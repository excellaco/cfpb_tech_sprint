# Imports
from faker import Faker

import pandas as pd
import os

# Bill Generation Process
# OCR software read bills in and provided a CSV of each bill, separating the lines of the bill into different rows.
# We manually assigned metadata to each separated line. Metadata included two additional columns.
#   1st Column: Bill Category. This gives us insight on what type of bill we are working with.
#   2nd Column: Line Type. This line type can be either constant_text, random_metric_text, random_nunber_for_metric_text, account_number, client_name, service_name, client_address, or service_address.

# Outside of the CSV, we also take note of the account number format. (i.e. Cell Phone may be ###-##-####, as electric may be ##### ##)
# In addition, we summarize the bill categories and provide each bill category a format for text generation.

class GenerateBillData:    
    def __init__(self):     
        self.new_line = '\n'
        self.new_line_2 = self.new_line + self.new_line
        self.constant_text_sentences = []
        self.bill_format = []
        self.csv_path = os.getenv("CSV_PATH", "../data/final_data/csvs_for_loading_data/")
        self.bill_format_csv_path = os.getenv("BILL_FORMAT_PATH", "../data/final_data/bill_format/")

    # This is for random metric text to provide a number.
    def generate_random_number(self):
        pass
    
    def generate_name(self):
        return fake.name()
    
    def generate_address(self):
        return fake.address()
        
    def read_csvs_and_populate_constant_text(self):
        for file_name in os.listdir(self.csv_path):
            file_path = self.csv_path + file_name
            file_to_process = pd.read_csv(file_path)
            
            for index, row in file_to_process.iterrows():
                data = row[0]
                line_type = row[1]
                
                if (line_type == 'constant_text'):
                    self.constant_text_sentences.append(data)
                
        self.constant_text_sentences = list(set(self.constant_text_sentences))
        print(self.constant_text_sentences)  
    
    # Blueprint for how we will generate a bill. Returns a list of values that contains line types.
    def retrieve_bill_format(self):
        pass
    
    # Logic to generate bill.
    def generate_bill(self, bill_format):
        generated_bill = ''
        
        for item in bill_format:
            if (item == 'constant_text'):
                # Retrieve random constant text from that Bill Category.
                pass
        
        return generated_bill             
    
    def execute_pipeline(self):
        retrieve_bill_format()
        read_csvs_and_populate_constant_text()
        
        # Generate Bills
        
    
            