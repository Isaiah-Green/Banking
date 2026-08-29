import random
import datetime
from Account import account
import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()
url: str = os.environ.get("DATABASE_URL")
key: str = os.environ.get("DATABASE_API_SECRET")

supabase: Client = create_client(url, key)

class Customer:
    def __init__(self , username=None, password= None, userID = None , entry_number = 0):
        self.User_Name = username
        self.password = password
        if userID == None:
            self._User_ID = random.randint(100000000 , 999999999)
        else:
            self._User_ID = userID
        self.credit_borrow = 0.0
        self.credit_score = 0
        self.add_entry(entry_number)
    #Loaded_customer = [UserID:  , UserName:    , Password:  , Credit Borrowed:   , Credit Score: ]  
    def load_customer(self , userName = None, password = None):
        response = supabase.table("Customer-List").select("*").eq("UserName" , userName).eq("Password" , password).execute()
        self._User_ID = response.data[0]["UserID"]
        self.User_Name = response.data[0]["UserName"]
        self.password = response.data[0]["Password"]
        self.credit_borrow = response.data[0]["Credit-Borrowed"]
        self.credit_score = response.data[0]["Credit-Score"]
    ####Functions that All Users will have access to
    def open_account(self , accountType, withdrawLim):
        response = supabase.table("Accounts").insert({
            "UserID": self._User_ID,
            "Account-Number": random.randint(1000, 9999), 
            "Account-Type": accountType,
            "Balance":  0.0,
            "Withdraw-Limit": withdrawLim
        }).execute()
    def add_entry(self , int):
        if int > 0 :
            response = supabase.table("Customer-List").insert({
                "UserID": self._User_ID ,
                "UserName":  self.User_Name,
                "Password" : self.password,
                "Credit-Borrowed": self.credit_borrow,
                "Credit-Score": self.credit_score
            }).execute()
        else:
            return 
    def close_account(self, accountNum, accountType):
        response = supabase.table("Accounts").delete().eq("UserID" , self._User_ID).eq("Account-Number" , accountNum).eq("Account-Type" , accountType).execute()
        ### Go in to the database and remove this entry 
    def change_accountType(self, newType, accountNum):
        response = supabase.table("Accounts").update({"Account-Type": newType}).eq("UserID" , self._User_ID).eq("Account-Number" , accountNum).execute()
        ### Go in to the database and update this information
    def view_accounts(self):
         response = supabase.table("Accounts").select("*").eq("UserID", self._User_ID).execute()
         return response.data
    def view_one_account(self, accountNum):
         response = supabase.table("Accounts").select("*").eq("UserID", self._User_ID).eq("Account=Number" , accountNum).execute()
         return response.data
    ##for testing currently

    
'''
Testing 

customer1 = Customer(username="WHOLETTHEDOG789*" , password="Ontheway64298!" , entry_number= 1)
customer2 = Customer(entry_number=0)
customer2.load_customer(userName="HImmers43#" , password="Twisteronthe54%")

customer1.open_account(accountType="Checking" , withdrawLim= 500)
print(customer1.view_accounts())

customer2.open_account(accountType="Savings" , withdrawLim= 100)
print(customer2.view_accounts())
'''

