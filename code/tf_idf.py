# ################################################################################################
# Imports
# ################################################################################################

import glob
import os
import pandas as pd
import nltk
import numpy as np
nltk.download('stopwords')

from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ################################################################################################
# Helper Functions
# ################################################################################################

def read_file(file_name):
    with open(file_name + '.txt','r') as f:
        data = f.read()

    return data

# ################################################################################################
# Defining Variables
# ################################################################################################

new_line = '\n'
new_line_2 = new_line + new_line

bills_path = os.getenv("WRITE_BILLS_PATH", "../data/final_data/bills/")
text_files = glob.glob(bills_path + "*.txt")

# Setting up data
file_names = []
[file_names.append(x[:-4]) for x in text_files]

file_data = []
[file_data.append(read_file(x)) for x in file_names] 

# Create a dataframe from the two lists above.
data = {'file_names': file_names, 'file_data':file_data} 
df = pd.DataFrame(data)

# ################################################################################################
# ML Portion
# ################################################################################################

# Creating corpus
corpus = [] 

for i in range(df['file_data'].size):
    corpus.append(df['file_data'][i])

# Stopwords are the English words which does not add much meaning to a sentence.
stop_words = stopwords.words('english')

vectorizer = TfidfVectorizer(stop_words = stop_words)
X = vectorizer.fit_transform(corpus)
X.todense() # Convert from sparse to dense matrix.

# Transform a count matrix to a normalized tf or tf-idf representation
# The goal of using tf-idf instead of the raw frequencies of occurrence of a token in a given document is to scale down the impact of tokens that occur very frequently in a given corpus and that are hence empirically less informative 
# than features that occur in a small fraction of the training corpus.
tfidf_transformer = TfidfTransformer(smooth_idf=True, use_idf=True)
tfidf_transformer.fit(X)
idf = tfidf_transformer.idf_

# Print idf values
df_idf = pd.DataFrame(tfidf_transformer.idf_, index=vectorizer.get_feature_names(), columns=["idf_weights"])

# Entire dataframe of files.
tf_idf_vector = tfidf_transformer.transform(X)

# Retrieve similarities of dataframe above and convert it to a dataframe
cosine_matrix = cosine_similarity(tf_idf_vector)

file_similarity_df = pd.DataFrame(data=cosine_matrix, columns=file_names, index=file_names)

# Retrieve second highest value for each row since when documents match to themselves, it will always be one.
file_similarity_df['max_value'] = file_similarity_df.apply(lambda row: row.nlargest(2).values[-1], axis=1)
result_df = file_similarity_df[file_similarity_df['max_value'] > 0.3]

suspicious_documents = result_df.index.tolist()

print(suspicious_documents)

# ################################################################################################
# End
# ################################################################################################