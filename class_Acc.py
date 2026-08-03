class Account:
    def __init__(self, account_number, account_password):
        self.account_number = account_number
        # The double (__) in front of account_password
        # sets the privacy of the attribute and makes it a private attribute.
        # It can only be accessed within the class and not outside the class.
        
acc1 = Account(123456, "mypassword")
print(acc1.account_number) #prints the account number
print(acc1.get_account_password()) # access via getter