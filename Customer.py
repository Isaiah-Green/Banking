import random
from Account import account
class Customer:
    def __init__(self , username, password , userID= None):
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
        for i in enumerate(self._accounts):
            if self._accounts[i].get_accountNumber  == accountNum and self._accounts[i].get_accountType == accountType:
                self._accounts.pop(i)
        ### Go in to the database and remove dthis entry 
    def change_accountType(self, newType, accountNum):
        for i in enumerate(self._accounts):
            if self._accounts[i].get_accountNumber  == accountNum:
                self._accounts[i].change_type(newType)
        ### Go in to the database and update this information
    def view_accounts(self):
        for i in enumerate(self._accounts):
            print(f"----------------------------------------")
            print(f" Account {i+1}: ")
            self._accounts[i].print_acc()
            print(f"----------------------------------------")
    def get_accounts(self):
        return self._accounts 
    def view_one_account(self, accountNum):
        for i in enumerate(self._accounts):
            if self._accounts[i].get_accountNumber() == accountNum:
                print(f"----------------------------------------")
                print(f" Account {self._accounts[i].get_accountNumber()}: ")
                self._accounts[i].print_acc()
                print(f"----------------------------------------") 
    def set_withdraw_limit(self, limit):
        self._withdraw_limit = limit
    def get_withdraw_limit(self):
        return self._withdraw_limit
    
    