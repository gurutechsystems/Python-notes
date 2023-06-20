#Modules are simple python files that can be used in another python file or program just by referencing it.
#So, when the module is called in a python file, the code control goes to the module python file to excute the module.

# Note: install boto3 custom module with pip boto3
#control+space to get a list of what we can import
import boto3 #boto3 is custom module implemented by AWS
import util  #util is custom module implemented by us but in same folder.Create Util module 
from custom_module import commons #This is custom module implemented by us but in a different folder

# boto3 module example for custom modules
print('\n#Use case of boto3 custom module')
def list_s3_buckets():
    s3=boto3.resource('s3')
    for bucket in s3.buckets.all():
        print(bucket.name)

# custom module built by us
print('\n#Use case of custom module built by us')
def store_invoice_details(name,price,invoice_id):
    print('storing invoice details of the customer;{}, price:{}, invoice_id:{}'.format(name,price,invoice_id))
    util.grt_db_credentials_param(name='abcd')
    print("Got DB credentials secret")
    print("Establising db connection....")
    print("Storing the details into DB...")
    print("Successfully stored invoice details in the DB!")
    return True

def transfter_amount(account_number, amount):
    print("\n# custom module built by us in a seperate folder")
    print("Transferring the amount: {} to account: {}".format(account_number, amount))
    is_valid_account = commons.check_if_valid_account(account_number=account_number)
    if is_valid_account == True:
        print("Successfully sent the amount: {} to the account: {}".format(amount, account_number))
    else:
        print("Wrong account number!")

# print(boto3)
# list_s3_buckets()
# store_invoice_details(name="Ngembane", price="$150", invoice_id="invoice-12345")
transfter_amount(1234567890, 150)

