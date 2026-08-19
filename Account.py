import random
import datetime
def validate_string(input_val):
    if isinstance(input_val, str):
        return True
    else:
        return False
def validate_int(input_val):
    if isinstance(input_val, int):
        return True
    else:
        return False
class account:
    def __init__(self, user_id, accountType):
        self._User_Id = user_id
        self.account_num = random.randint(1000, 9999)
        self.accountType = accountType
        self.balance = 0.0
        self.dates = {}
    def account_import(self, accountTextLine):
        information = accountTextLine.split(" ")
        self._User_Id = information[1]
        self.accountType = information[9]
        self.account_num = information[5]
        self.balance = information[12]
        self.dates = information[16]
    def add_bal(self, amount):
        now = datetime.datetime.now()
        self.dates.update({now : f"Add Balance: {amount}"})
        if validate_int(amount):
            self.balance += amount
            return True
        else:
            return False
    def remove_bal(self, amount):
        now = datetime.datetime.now()
        self.dates.update({now : f"Remove Balance: {amount}"})
        if validate_int(amount):
            self.balance -= amount
            return True
        else:
            return False
    def change_type(self, accountType):
        now = datetime.datetime.now()
        self.dates.update({now : "Change Account Type"})
        if validate_string(accountType):
            if (accountType == "Savings" or "Checking" or "Credit"):
                self.accountType = accountType
                return True
        else:
            return False
    def get_bal(self):
        return self.balance
    def get_accountType(self):
        return self.accountType
    def get_accountNumber(self):
        return self.account_num
    def print_acc(self):
        return f"[UserID: {self._User_Id} , Account Number: {self.account_num} , Account Type: {self.accountType} , Balance: {self.balance} , Dates Accessed: {self.dates}]"


'''
Testing

imported_account = "[UserID: 765243897 , Account Number: 3165 , Account Type: Credit , Balance: 854000 , Dates Accessed: ]"
my_account = account(879657889 , "Checking")
print(my_account.print_acc())
my_account.add_bal(6000)
my_account.remove_bal(1000)
my_account.change_type("Savings")
print(my_account.print_acc())
print(my_account.get_bal())
print(my_account.get_accountType())
print(my_account.get_accountNumber())
my_account.account_import(imported_account)
print(my_account.print_acc())
'''