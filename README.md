# cfpb_tech_sprint

### Code folder

Contains the following files:
1. PDF_text_extraction.ipynb - python notebook for extracting text from .pdf documents and saving in .csv format
2. generate_bill_data.py - python script for generating large numbers of unique simulated utility bills
3. generate_pepco_bills.py - python script for generating large numbers of near-identical simulated utility bills
4. tf_idf.py - python model script for transforming a large document corpus into document-level TF-IDF vector representations, creating a document-document cosine similarity matrix, and using the matrix to identify highly similar documents
5. model_analysis.ipynb - python notebook containing another variant of the same TF-IDF / Cosine Similarity model.  This notebook contains visualizations of the cosine similarity distribution for the unique and near-identical simulated utility bill distributions.  These visualizations help a user to determine the threshold value for identifying similar documents

### Data folder
Contains two subfolders:
1. Initial Ideas - contains raw collection of base documents and text extraction .csv files
2. Final Data - Contains select collection of base documents, related text extraction .csv files, and model output files
