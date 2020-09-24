# Bill Generation Process
# OCR software read bills in and provided a CSV of each bill, separating the lines of the bill into different rows.
# We manually assigned metadata to each separated line. Metadata included two additional columns.
#   1st Column: Bill Category. This gives us insight on what type of bill we are working with.
#   2nd Column: Line Type. This line type can be either constant_text, random_metric_text, random_nunber_for_metric_text, account_number, client_name, service_name, client_address, or service_address.

# Outside of the CSV, we also take note of the account number format. (i.e. Cell Phone may be ###-##-####, as electric may be ##### ##)
# In addition, we summarize the bill categories and provide each bill category a format for text generation.

from faker import Faker

class GenerateBillData:    
    def __init__(self):     
        self.new_line = '\n'
        self.new_line_2 = self.new_line + self.new_line
        self.bill_categories = []
        self.bill_category_constant_text = {}
        self.bill_category_random_metric_text = {}
    
    # Based on the bill categories available, for the bill we read in, what type of bill is it.
    def retrieve_bill_categories(self):        
        print('Retrieving bill categories.')
        self.bill_categories = ['Electric', 'Gas', 'Cellular']
        
        return 'Electric'
    
    # Build up dictionary of constant text.
    def retrieve_constant_text_per_bill_category(self):
        # Append to dictionary bill_category_constant_text
        pass
        
    # Return a list of words that are captured as words we would see in random metrix text for each bill category. 
    def retrieve_random_metric_text_per_bill_category(self):
        # Append to dictionary bill_category_random_metric_text
        pass
    
    # This is for random metric text to provide a number.
    def generate_random_number(self):
        pass
    
    # Blueprint for how we will generate Bill. Return list of values that contain line types. 
    def retrieve_bill_format_per_bill_category(self, bill_category):
        pass
    
    def generate_name(self):
        return fake.name()
    
    def generate_address(self):
        return fake.address()
        
    def generate_bill(self, bill_format, bill_category):
        generated_bill = ''
        
        for item in bill_format:
            if (item == 'constant_text'):
                # Retrieve random constant text from that Bill Category.
                pass
        
        return generated_bill
                
    
    def execute_pipeline():
        # Building up catalog that will allow us to generate bills.
        retrieve_bill_categories()
        retrieve_constant_text_per_bill_category()
        retrieve_random_metric_text_per_bill_category()
        
        # Generate Electric Bills
        electric_bill_format = retrieve_bill_format_per_bill_category('Electric')
        generated_electric_bill = generate_bill(electric_bill_format, 'Electric')
        
    
            