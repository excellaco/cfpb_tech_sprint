# ################################################################################################
# Imports
# ################################################################################################

import glob
import os
import pandas as pd
import nltk
import numpy as np
from collections import defaultdict

nltk.download("stopwords")

from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ################################################################################################
# Helper Functions
# ################################################################################################


def read_file(file_name):
    with open(file_name + ".txt", "r") as f:
        data = f.read()

    return data


# ################################################################################################
# Defining Variables
# ################################################################################################

new_line = "\n"
new_line_2 = new_line + new_line

bills_path = os.getenv("WRITE_BILLS_PATH", "../data/final_data/pepco_bills/")
model_output_path = os.getenv("MODEL_OUTPUT_PATH", "../data/final_data/output/")
text_files = glob.glob(bills_path + "*.txt")

# Setting up data
file_names = []
[file_names.append(x[:-4]) for x in text_files]

file_data = []
[file_data.append(read_file(x)) for x in file_names]

# Create a dataframe from the two lists above.
data = {"file_names": file_names, "file_data": file_data}
df = pd.DataFrame(data)

# ################################################################################################
# ML Portion
# ################################################################################################

# Creating corpus. (Collection of text)
corpus = []

for i in range(df["file_data"].size):
    corpus.append(df["file_data"][i])

# Stopwords are the English words which does not add much meaning to a sentence.
stop_words = stopwords.words("english")

# Tf-idf focuses on more relevant words.
vectorizer = TfidfVectorizer(stop_words=stop_words)
X = vectorizer.fit_transform(corpus)
X.todense()  # Convert from sparse to dense matrix.

# Transform a count matrix to a normalized tf or tf-idf representation
# The goal of using tf-idf instead of the raw frequencies of occurrence of a token in a given document is to scale down the impact of tokens that occur very
# frequently in a given corpus and that are hence empirically less informative
# than features that occur in a small fraction of the training corpus.
tfidf_transformer = TfidfTransformer(smooth_idf=True, use_idf=True)
tfidf_transformer.fit(X)

# Entire dataframe of files.
tf_idf_vector = tfidf_transformer.transform(X)

# Retrieve similarities of dataframe above and convert it to a dataframe
cosine_matrix = cosine_similarity(tf_idf_vector)
file_similarity_df = pd.DataFrame(
    data=cosine_matrix, columns=file_names, index=file_names
)

# Retrieve second highest value for each row since when documents match to themselves, it will always be one. Threshold was set to .35.
file_similarity_df["max_value"] = file_similarity_df.apply(
    lambda row: row.nlargest(2).values[-1], axis=1
)
result_df = file_similarity_df[file_similarity_df["max_value"] > 0.30]

# Retrieve the list of all potential suspicious documents and update a dictionary with the document name & score.
suspicious_documents = result_df.index.tolist()
suspicious_document_scores = {}

for document_name in suspicious_documents:

    if document_name in result_df.index:
        values_dict = result_df["max_value"].to_dict()

        for key, value in values_dict.items():

            if key == document_name:
                document_name_index = document_name.rfind("/")
                document_name = document_name[document_name_index + 1 :].strip()
                suspicious_document_scores.update({document_name: value})

# Remove values that appear once because we want to map all suspicious documents with one another. Need a count of 2 or higher.
suspicious_document_scores_df = pd.DataFrame(
    list(suspicious_document_scores.items()), columns=["file_name", "sus_score"]
)
suspicious_document_scores_df = suspicious_document_scores_df[
    suspicious_document_scores_df.groupby("sus_score").sus_score.transform(len) > 1
]

# Group concat to get the combinations.
suspicious_document_scores_df = suspicious_document_scores_df.groupby("sus_score").agg(
    {"file_name": lambda x: ", ".join(x)}
)

suspicious_document_scores_df = suspicious_document_scores_df.rename(
    columns={"file_name": "suspicious_matches"}
)
suspicious_document_scores_df.to_csv(
    model_output_path + "tfidf_cosine_similarity_results.csv", index=False
)

print(suspicious_document_scores_df)

# ################################################################################################
# End
# ################################################################################################
