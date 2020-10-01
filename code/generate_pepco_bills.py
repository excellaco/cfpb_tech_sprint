# Imports
from faker import Faker

import pandas as pd
import os
import random
from datetime import datetime, timedelta

class GeneratePepcoBills:
    def __init__(self):
        self.new_line = "\n"
        self.new_line_2 = self.new_line + self.new_line

        # Different Lists
        self.constant_account_number_text = ["Account Number:"]
        self.constant_intro_text = ["Delmarva Power: Exelon Company", "Pepco"]
        self.constant_electric_bill_header_text = ["Your electric bill - "]
        self.constant_electric_bill_header_footer_text = ["for the period "]
        self.constant_tag_line_text = [
            "Energy for a Changing World.",
            "Ways to save - Find tips and programs that help.",
        ]
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
            "Your smart electric meter is read wirelessly. Visit My Account at pepco.com to view your daily and hourly energy usage. \nIf you are moving or discontinuing service, please contact Pepco at least three days in advance. \nInformation regarding rate schedules and how to verify the accuracy of your bill will be mailed upon request. \nFollow us on Twitter at twitter.com/PepcoConnect. Like us on Facebook at facebook.com/PepcoConnect. \nThe EmPOWER MD charge funds programs that can help you reduce your energy consumption and save you money. For more information, including how to participate, go to pepco.com/saveenergy.",
            "Your smart electric meter is read wirelessly. Visit My Account at pepco.com to view your daily and hourly energy usage. \nIf you are moving or discontinuing service, please contact Pepco at least three days in advance. \nInformation regarding rate schedules and how to verify the accuracy of your bill will be mailed upon request. \nFollow us on Twitter at twitter.com/PepcoConnect. Like us on Facebook at facebook.com/PepcoConnect.",
            "Find helpful storm preparation and power outage information at delmarva.com  Learn how to save energy and money by registering for MyAccount at www.delmarva.com. Your smart meter is read wirelessly. Visit My Account at delmarva.com to view your daily and hourly energy usage. The EmPOWER MD charge funds programs that can help you reduce your energy consumption and save you money. For more information, including how to participate, go to delmarva.com/saveenergy.",
        ]

        # Variable After Lists
        self.constant_charge_summary_text = ["Summary of your charges"]
        self.constant_contact_info_text = [
            "How to contact us. \nCustomer Service (Mon-Fri,7am - 8 pm)\t202-833-7500\n.  Hearing Impaired (TTY)\t202-872-2369\n.  ¿Problemas con la factura?\t202-872-4641\nElectric emergencies & outages (24 hours)\t1-877-737-2662\nVisit pepco.com for service, billing and correspondence information."
        ]
        self.constant_electricy_info_text = [
            "Your monthly Electricity use in kWh\nDaily temperature averages: "
        ]

        # Additional Variables
        self.n_documents_generated = 2500

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
        result = (
            "After "
            + self.generate_date()
            + " a Late Payment Charge of $"
            + str(random.uniform(0.00, 99.99))
            + " will be added, increasing the amount due to $"
            + str(random.uniform(0.00, 99.99))
            + "."
        )

        return result

    def generate_name(self):
        return self.fake.name()

    def generate_address(self):
        return self.fake.address()

    def generate_random_date_range_text(self):
        date_range_text = self.generate_date() + " to " + self.generate_date()
        return date_range_text

    def generate_temp_range(self):
        result = str(random.randint(50, 99)) + " to " + str(random.randint(100, 120))
        return result

    # Blueprint for how we will generate a bill. Returns a list of values that contains line types.
    def retrieve_bill_format_and_generate_bill(self):

        generated_bill_text = ""

        random_account_number = self.generate_account_number()
        random_name = self.generate_name()
        random_pepco_address = 'PO BOX 13608\nPHILADELPHIA PA 19101'
        random_service_address = self.generate_address()
        random_date_range = self.generate_random_date_range_text()

        random_date_one = self.generate_date()
        random_date_two = self.generate_date()
        random_date_three = self.generate_date()

        random_date = [random_date_one, random_date_two, random_date_three]

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
                        generated_bill_text = generated_bill_text

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

                    elif variable_after == "black_line_text":
                        generated_bill_text = (
                            generated_bill_text
                            + "---------------------------------------------------------------------------------------------------"
                            + self.new_line_2
                        )

                    elif variable_after == "charge_summary_text":
                        generated_bill_text = (
                            generated_bill_text
                            + random.choice(self.constant_charge_summary_text)
                            + self.new_line_2
                        )

                    elif variable_after == "contact_info_text":
                        generated_bill_text = (
                            generated_bill_text
                            + random.choice(self.constant_contact_info_text)
                            + self.new_line_2
                        )

                    elif variable_after == "customer_name":
                        generated_bill_text = (
                            generated_bill_text + random_name + self.new_line_2
                        )

                    elif variable_after == "date_range_text":
                        generated_bill_text = (
                            generated_bill_text + random_date_range + self.new_line_2
                        )

                    elif variable_after == "electricity_info_text":
                        generated_bill_text = (
                            generated_bill_text
                            + random.choice(self.constant_electricy_info_text)
                            + self.generate_temp_range()
                            + self.new_line_2
                        )

                    elif variable_after == "full_date_text":
                        generated_bill_text = (
                            generated_bill_text
                            + random.choice(random_date)
                            + self.new_line_2
                        )

                    elif variable_after == "general_text_after_payments":
                        generated_bill_text = (
                            generated_bill_text
                            + random.choice(self.general_text_after_payment)
                            + self.new_line_2
                        )

                    elif variable_after == "intro_text":
                        generated_bill_text = (
                            generated_bill_text
                            + random.choice(self.constant_intro_text)
                            + self.new_line_2
                        )

                    elif variable_after == "invoice_footer_text":
                        generated_bill_text = (
                            generated_bill_text
                            + "Invoice Number: "
                            + str(random.randint(100000000000, 999999999999))
                            + "\tPage 1"
                            + self.new_line_2
                        )

                    elif variable_after == "late_payment_text":
                        generated_bill_text = (
                            generated_bill_text
                            + self.generate_late_payment_notice()
                            + self.new_line_2
                        )

                    elif variable_after == "mailer_text":
                        generated_bill_text = (
                            generated_bill_text
                            + random_name
                            + "\n"
                            + random_service_address
                            + self.new_line_2
                        )

                    elif variable_after == "month_date_text":
                        generated_bill_text = (
                            generated_bill_text
                            + random.choice(random_date)
                            + self.new_line_2
                        )

                    elif variable_after == "page_footer_text":
                        generated_bill_text = (
                            generated_bill_text
                            + str(random.randint(100000000000, 999999999999))
                            + self.new_line_2
                        )

                    elif variable_after == "price_text":
                        generated_bill_text = (
                            generated_bill_text
                            + str(random.uniform(0.00, 99.99))
                            + self.new_line_2
                        )

                    elif variable_after == "return_coupon_text":
                        generated_bill_text = (
                            generated_bill_text
                            + "Return this coupon with your payment made payable to Pepco"
                            + self.new_line_2
                        )

                    elif variable_after == "service_address_text":
                        generated_bill_text = (
                            generated_bill_text
                            + random_service_address
                            + self.new_line_2
                        )

                    elif variable_after == "tag_line_text":
                        generated_bill_text = (
                            generated_bill_text
                            + random.choice(self.constant_tag_line_text)
                            + self.new_line_2
                        )

                    elif variable_after == "electric_charge_details_constant_text":
                        generated_bill_text = (
                            generated_bill_text
                            + "Details of your Electric Charges "
                            + self.new_line_2
                        )

                    elif variable_after == "electric_charge_details_variable_text":
                        generated_bill_text = (
                            generated_bill_text
                            + str(random.randint(1, 25))
                            + " charge types; "
                            + str(random.randint(200, 999))
                            + " KWH; "
                            + str(random.randint(10, 120))
                            + " Full Total."
                            + self.new_line_2
                        )

                    elif variable_after == "final_footer":
                        generated_bill_text = (
                            generated_bill_text
                            + "Your daily electricity use for this bill period. Visit My Account at pepco.com to see your hourly electricity use"
                            + self.new_line_2
                        )
                        
                    elif variable_after == "pepco_address_text":
                        generated_bill_text = (
                            generated_bill_text
                            + random_pepco_address
                            + self.new_line_2
                        )

        with open(self.write_bills_path + file_name_for_generation + ".txt", "w+") as f:
            f.write(generated_bill_text)

    def execute_pipeline(self):
        for _ in range(self.n_documents_generated):
            self.retrieve_bill_format_and_generate_bill()
