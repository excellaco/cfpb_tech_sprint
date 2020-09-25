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
        self.new_line = "\n"
        self.new_line_2 = self.new_line + self.new_line

        # Different Text Types
        self.constant_account_number_text = []
        self.constant_address_text = []
        self.constant_bill_header_text = []
        self.constant_concat_text = []
        self.constant_date_text = []
        self.constant_general_text = []
        self.constant_header_text = []
        self.constant_intro_text = []
        self.constant_int_usage_text = []
        self.constant_misc_phrase_text = []
        self.constant_page_header_text = []
        self.constant_price_text = []
        self.constant_range_text = []
        self.unknown_text = []

        self.bill_format = []
        self.csv_path = os.getenv(
            "CSV_PATH", "../data/final_data/csvs_for_loading_data/"
        )
        self.bill_format_csv_path = os.getenv(
            "BILL_FORMAT_PATH", "../data/final_data/bill_format/"
        )

    # This is for random metric text to provide a number.
    def generate_random_number(self):
        pass

    def generate_name(self):
        return fake.name()

    def generate_address(self):
        return fake.address()

    def read_csvs_and_populate_constant_text(self):
        for file_name in os.listdir(self.csv_path):
            if file_name.endswith(".csv"):
                file_path = self.csv_path + file_name
                file_to_process = pd.read_csv(file_path)

                concat_sentence = ""
                current_text_type = ""

                # Concat sentences and add to lists above.
                for index, row in file_to_process.iterrows():

                    index_number = index
                    file_name = row["filename"]
                    page = row["page"]
                    block = row["block"]
                    line = row["line"]
                    word = row["word"]
                    text = row["text"]
                    unknown_character_flag = row["unknown_character"]
                    unknown_digit_flag = row["unknown_digit"]
                    name_flag = row["name"]
                    address_flag = row["address"]
                    date_flag = row["date"]
                    year_flag = row["year"]
                    price_flag = row["price"]
                    account_number_flag = row["account_number"]
                    int_usage_flag = row["int_usage"]
                    misc_phrase_flag = row["misc_phrase"]
                    text_type = row["text_type"]

                    if (text_type == current_text_type and text_type != 'Variable'):
                        concat_sentence = concat_sentence + " " + text
                    else:
                        if (current_text_type == 'AccountNumberText'):
                            self.constant_account_number_text.append(concat_sentence.lstrip())
                        elif (current_text_type == 'AddressText'):
                            self.constant_address_text.append(concat_sentence.lstrip())
                        elif (current_text_type == 'AddressText'):
                            self.constant_address_text.append(concat_sentence.lstrip())
                        elif (current_text_type == 'BillHeader'):
                            self.constant_bill_header_text.append(concat_sentence.lstrip())
                        elif (current_text_type == 'ConcatText'):
                            self.constant_concat_text.append(concat_sentence.lstrip())
                        elif (current_text_type == 'DateText'):
                            self.constant_date_text.append(concat_sentence.lstrip())
                        elif (current_text_type == 'GeneralText'):
                            self.constant_general_text.append(concat_sentence.lstrip())
                        elif (current_text_type == 'HeaderText'):
                            self.constant_header_text.append(concat_sentence.lstrip())
                        elif (current_text_type == 'Intro'):
                            self.constant_intro_text.append(concat_sentence.lstrip())
                        elif (current_text_type == 'IntUsageText'):
                            self.constant_int_usage_text.append(concat_sentence.lstrip())
                        elif (current_text_type == 'MiscPhraseText'):
                            self.constant_misc_phrase_text.append(concat_sentence.lstrip())
                        elif (current_text_type == 'PageHeader'):
                            self.constant_page_header_text.append(concat_sentence.lstrip())
                        elif (current_text_type == 'PriceText'):
                            self.constant_price_text.append(concat_sentence.lstrip())
                        elif (current_text_type == 'RangeText'):
                            self.constant_range_text.append(concat_sentence.lstrip())
                        else:
                            self.unknown_text.append(concat_sentence.lstrip())
                            
                    
                    # Needed to properly loop through logic up top.
                    if (text_type != 'Variable'):
                        current_text_type = text_type
                    else:
                        concat_sentence = ''
                        current_text_type = ''

        # Distinct out lists.
        self.constant_account_number_text = list(set(self.constant_account_number_text))
        self.constant_bill_header_text = list(set(self.constant_bill_header_text))
        self.constant_concat_text = list(set(self.constant_concat_text))
        self.constant_date_text = list(set(self.constant_date_text))
        self.constant_general_text = list(set(self.constant_general_text))
        self.constant_header_text = list(set(self.constant_header_text))
        self.constant_intro_text = list(set(self.constant_intro_text))
        self.constant_int_usage_text = list(set(self.constant_int_usage_text))
        self.constant_misc_phrase_text = list(set(self.constant_misc_phrase_text))
        self.constant_page_header_text = list(set(self.constant_page_header_text))
        self.constant_price_text = list(set(self.constant_price_text))
        self.constant_range_text = list(set(self.constant_range_text))
        self.unknown_text = list(set(self.unknown_text))

        #print(self.constant_concat_text)

    # Blueprint for how we will generate a bill. Returns a list of values that contains line types.
    def retrieve_bill_format(self):
        pass

    # Logic to generate bill.
    def generate_bill(self, bill_format):
        generated_bill = ""

        for item in bill_format:
            if item == "constant_text":
                # Retrieve random constant text from that Bill Category.
                pass

        return generated_bill

    def execute_pipeline(self):
        retrieve_bill_format()
        read_csvs_and_populate_constant_text()

        # Generate Bills
