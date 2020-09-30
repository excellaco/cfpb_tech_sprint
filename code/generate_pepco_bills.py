# Imports
from faker import Faker

import pandas as pd
import os
import random
from datetime import datetime, timedelta

# Bill Generation Process
# OCR software read bills in and provided a CSV of each bill, separating the lines of the bill into different rows.
# We manually assigned metadata to each separated line. Metadata included two additional columns.
#   1st Column: Bill Category. This gives us insight on what type of bill we are working with.
#   2nd Column: Line Type. This line type can be either constant_text, random_metric_text, random_nunber_for_metric_text, account_number, client_name, service_name, client_address, or service_address.

# Outside of the CSV, we also take note of the account number format. (i.e. Cell Phone may be ###-##-####, as electric may be ##### ##)
# In addition, we summarize the bill categories and provide each bill category a format for text generation.


class GeneratePepcoBills:
    def __init__(self):
        self.new_line = "\n"
        self.new_line_2 = self.new_line + self.new_line

        # Different Lists
        self.constant_account_number_text = ["Account Number:"]
        self.constant_intro_text = ["Delmarva Power: Exelon Company", "Pepco"]
        self.constant_electric_bill_header_text = ["Your electric bill - "]
        self.constant_electric_bill_header_footer_text = ["for the period "]
        self.constant_tag_line_text = ["Energy for a Changing World."]
        self.constant_service_address_text = ["Your service Address:"]
        self.constant_bill_issue_date_text = ["Bill Issue date: "]
        self.constant_last_bill_balance_text = ["Balance from your last bill "]
        self.constant_posted_payment_text = ["Your payment(s) - thank you "]
        self.constant_balance_forward_text = ["Balance forward as of "]
        self.constant_new_charges_text = ["New electric charges "]
        self.constant_new_credits_text = ["New Neighborhood Sun Credits "]
        self.constant_total_amount_due_text = ["Total amount due by "]
        self.constant_invoice_footer_text = ["Please tear on the dotted line below."]

        # General Lists
        self.general_text_after_payment = [
            "Your smart electric meter is read wirelessly. Visit My Account at pepco.com to view your daily and hourly energy usage. If you are moving or discontinuing service, please contact Pepco at least three days in advance. Information regarding rate schedules and how to verify the accuracy of your bill will be mailed upon request. Follow us on Twitter at twitter.com/PepcoConnect. Like us on Facebook at facebook.com/PepcoConnect. The EmPOWER MD charge funds programs that can help you reduce your energy consumption and save you money. For more information, including how to participate, go to pepco.com/saveenergy.",
            "Find helpful storm preparation and power outage information at delmarva.com  Learn how to save energy and money by registering for MyAccount at www.delmarva.com. Your smart meter is read wirelessly. Visit My Account at delmarva.com to view your daily and hourly energy usage. The EmPOWER MD charge funds programs that can help you reduce your energy consumption and save you money. For more information, including how to participate, go to delmarva.com/saveenergy.",
        ]

        # Variable After Lists
        self.n_documents_generated = 3

        self.bill_format_csv_path = os.getenv(
            "BILL_FORMAT_PATH", "../data/final_data/bill_format/"
        )

        self.write_bills_path = os.getenv(
            "WRITE_BILLS_PATH", "../data/final_data/pepco_bills/"
        )

        self.fake = Faker()

    def generate_date(self, min_year=2015, max_year=datetime.now().year):
        # generate a datetime in format yyyy-mm-dd hh:mm:ss.000000
        start = datetime(min_year, 1, 1, 00, 00, 00)
        years = max_year - min_year + 1
        end = start + timedelta(days=365 * years)

        generated_date = str(start + (end - start) * random.random())
        generated_date = generated_date[:10]

        return generated_date

    # This is for generating an account number
    def generate_account_number(self):
        random_number = str(random.randint(100000000, 999999999))

        random_number = random_number[:1] + "-" + random_number[1:]
        random_number = random_number[:6] + "-" + random_number[6:]

        return random_number

    def generate_late_payment_notice(self):
        pass

    def generate_name(self):
        return self.fake.name()

    def generate_address(self):
        return self.fake.address()

    def generate_random_date_range_text(self):
        date_range_text = self.generate_date() + " to " + self.generate_date()
        return date_range_text

    # Blueprint for how we will generate a bill. Returns a list of values that contains line types.
    def retrieve_bill_format_and_generate_bill(self):

        generated_bill_text = ""

        random_account_number = self.generate_account_number()
        random_name = self.generate_name()
        random_client_address = self.generate_address()
        random_service_address = self.generate_address()
        random_name_address = [random_name, random_client_address]
        file_name_for_generation = random_name + "-" + random_account_number
        file_name_for_generation = file_name_for_generation.replace(" ", "_")

        for file_name in os.listdir(self.bill_format_csv_path):
            if file_name.endswith(".csv"):
                file_path = self.bill_format_csv_path + file_name
                file_to_process = pd.read_csv(file_path)

                # Concat sentences and add to lists above.
                for index, row in file_to_process.iterrows():

                    index_number = index
                    bill_format = row["bill_format"]
                    variable_after = row["variable_after"]

                    # Bill Format
                    if bill_format == "AccountNumberText":
                        generated_bill_text = (
                            generated_bill_text
                            + random.choice(self.constant_account_number_text)
                            + self.new_line_2
                        )

                    elif bill_format == "BalanceForwardText":
                        generated_bill_text = (
                            generated_bill_text
                            + random.choice(self.constant_balance_forward_text)
                            + self.new_line_2
                        )

                    elif bill_format == "Bill_Issue_Date_Text":
                        generated_bill_text = (
                            generated_bill_text
                            + random.choice(self.constant_bill_issue_date_text)
                            + self.new_line_2
                        )

                    elif bill_format == "ElectricBillHeader":
                        generated_bill_text = (
                            generated_bill_text
                            + random.choice(self.constant_electric_bill_header_text)
                            + self.new_line_2
                        )

                    elif bill_format == "ElectricBillHeaderFooter":
                        generated_bill_text = (
                            generated_bill_text
                            + random.choice(
                                self.constant_electric_bill_header_footer_text
                            )
                            + self.new_line_2
                        )

                    elif bill_format == "InvoiceFooterText":
                        generated_bill_text = (
                            generated_bill_text
                            + random.choice(self.constant_invoice_footer_text)
                            + self.new_line_2
                        )

                    elif bill_format == "LastBillBalanceText":
                        generated_bill_text = (
                            generated_bill_text
                            + random.choice(self.constant_last_bill_balance_text)
                            + self.new_line_2
                        )

                    elif bill_format == "NewChargesText":
                        generated_bill_text = (
                            generated_bill_text
                            + random.choice(self.constant_new_charges_text)
                            + self.new_line_2
                        )

                    elif bill_format == "NewCreditsText":
                        generated_bill_text = (
                            generated_bill_text
                            + random.choice(self.constant_new_credits_text)
                            + self.new_line_2
                        )

                    elif bill_format == "NoHeader":
                        pass

                    elif bill_format == "PostedPaymentText":
                        generated_bill_text = (
                            generated_bill_text
                            + random.choice(self.constant_posted_payment_text)
                            + self.new_line_2
                        )

                    elif bill_format == "ServiceAddressText":
                        generated_bill_text = (
                            generated_bill_text
                            + random.choice(self.constant_service_address_text)
                            + self.new_line_2
                        )

                    elif bill_format == "TagLine":
                        generated_bill_text = (
                            generated_bill_text
                            + random.choice(self.constant_tag_line_text)
                            + self.new_line_2
                        )

                    elif bill_format == "TotalAmountDueText":
                        generated_bill_text = (
                            generated_bill_text
                            + random.choice(self.constant_total_amount_due_text)
                            + self.new_line_2
                        )

                    # Variable After
                    if variable_after == "account_number_text":
                        generated_bill_text = (
                            generated_bill_text
                            + random_account_number
                            + self.new_line_2
                        )

                    elif variable_after == "client_address_text":
                        generated_bill_text = (
                            generated_bill_text
                            + random_client_address
                            + self.new_line_2
                        )

        with open(self.write_bills_path + file_name_for_generation + ".txt", "w+") as f:
            f.write(generated_bill_text)

    def execute_pipeline(self):
        for _ in range(self.n_documents_generated):
            self.retrieve_bill_format_and_generate_bill()
