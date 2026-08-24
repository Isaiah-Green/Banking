import random
import datetime
from Account import account

def Make_accountList(TextFile , userID):
    temp = []
    try:
        with open(TextFile , "r") as f:
            for line in f:
                y = line.split(" ")
                if int(y[1]) == userID:
                    temp.append(line)
    except FileNotFoundError:
        print("Error: The file does not exist.")
    return temp
class Customer:
    def __init__(self , username=None, password= None, userID = None):
        self._User_Name = username
        self._password = password
        if userID == None:
            self._User_ID = random.randint(100000000 , 999999999)
        else:
            self._User_ID = userID
        self.credit_borrow = 0.0
        self.credit_score = 0
        self._accounts = []
    #Loaded_customer = [UserID:  , UserName:    , Password:  , Credit Borrowed:   , Credit Score: ]  
    def load_customer(self , DBLine , AccountDBLineList):
        information = DBLine.split(" ")
        self.userID = information[1]
        self.credit_borrow = information[11]
        self.credit_score = information[15]
        self._User_Name = information[4]
        self._password = information[7]
        for item in AccountDBLineList:
            y = item.split(" ")
            temp_account = account(self._User_ID)
            temp_account.account_import(item)
            self._accounts.append(temp_account)
    ####Functions that All Users will have access to
    def open_account(self , accountType, withdrawLim):
        if withdrawLim < 0:
            withdrawLim = 0.0
        acct = account(self._User_ID,accountType, withdrawLim)
        self._accounts.append(acct)
        ## write into database 
    def close_account(self, accountNum, accountType):
        for i in range(len(self._accounts)):
            if self._accounts[i].get_accountNumber()  == accountNum and self._accounts[i].get_accountType() == accountType:
                self._accounts.pop(i)
                break
        ### Go in to the database and remove this entry 
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
    def set_withdraw_limit(self, accNum , limit):
        for i in range (len(self._accounts)):
            y = self._accounts[i].get_accountNumber()
            if y == accNum:
                self._accounts[i].set_withdraw(limit)
    def get_withdraw_limit(self , accNum):
        t = 0.0
        for i in range (len(self._accounts)):
            y = self._accounts[i].get_accountNumber()
            if y == accNum:
                t = self._accounts[i].get_withdraw()
        return t
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
print(customer.get_withdraw_limit(y[0]))
customer.open_account("Savings" , 1000)
y = customer.get_acct_num()
print(customer.get_withdraw_limit(y[1]))
customer.set_withdraw_limit(y[1], 200)
customer.view_accounts()
Loaded_customer = "[UserID: 876546756  , UserName: Igreen   , Password: Indig0 , Credit Borrowed: 200 , Credit Score: 145]"
customer2 =Customer()
print("-----------------------------")
list = Make_accountList("testing_accountfile" , 876546756)
customer2.load_customer("[UserID: 876546756  , UserName: Igreen   , Password: Indig0 , Credit Borrowed: 200 , Credit Score: 145]", list)
customer2.view_accounts()
'''