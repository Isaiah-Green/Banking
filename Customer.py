import random
import datetime
from Account import account
class Customer:
    def __init__(self , username, password , userID = None):
        self._User_Name = username
        self._Password = password
        if userID == None:
            self._User_ID = random.randint(100000000 , 999999999)
        else:
            self._User_ID = userID
        self.credit_borrow = 0.0
        self.credit_score = 0
        self._withdraw_limit = 0.0
        self._accounts = []
    ####Functions that All Users will have access to
    def open_account(self , accountType, withdrawLim):
        if withdrawLim < 0:
            self._withdraw_limit = 0.0
        else:
            self._withdraw_limit = withdrawLim
        acct = account(self._User_ID,accountType)
        self._accounts.append(acct)
        ## write into database 
    def close_account(self, accountNum, accountType):
        for i in range(len(self._accounts)):
            if self._accounts[i].get_accountNumber()  == accountNum and self._accounts[i].get_accountType() == accountType:
                self._accounts.pop(i)
                break
        ### Go in to the database and remove dthis entry 
    def change_accountType(self, newType, accountNum):
        for i in range(len(self._accounts)):
            if self._accounts[i].get_accountNumber()  == accountNum:
                self._accounts[i].change_type(newType)
        ### Go in to the database and update this information
    def view_accounts(self):
        for i in range(len(self._accounts)):
            print(f"----------------------------------------")
            print(f" Account {i}: ")
            t = self._accounts[i].print_acc()
            print(t)
            print(f"----------------------------------------")
    def get_accounts(self):
        return self._accounts 
    def view_one_account(self, accountNum):
        for i in range(len(self._accounts)):
            if self._accounts[i].get_accountNumber() == accountNum:
                print(f"----------------------------------------")
                print(f" Account {self._accounts[i].get_accountNumber()}: ")
                t = self._accounts[i].print_acc()
                print(t)
                print(f"----------------------------------------") 
    def set_withdraw_limit(self, limit):
        self._withdraw_limit = limit
    def get_withdraw_limit(self):
        return self._withdraw_limit
    ##for testing currently
    def get_acct_num(self):
        t = []
        for i in range(len(self._accounts)):
            y = self._accounts[i].get_accountNumber()
            t.append(y)
        return t

    
'''
Testing 
customer = Customer(username="Igreen" , password="Indig0")
customer.open_account("Checking" , 500)
customer.open_account("Savings" , 100)
customer.view_accounts()
y = customer.get_acct_num()
customer.change_accountType("Checking" , y[1])
customer.view_one_account(y[1])
customer.close_account(y[1] , "Checking")
customer.view_accounts()
'''
