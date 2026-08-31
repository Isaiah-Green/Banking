import random
import datetime
import os
from dotenv import load_dotenv
from supabase import create_client, Client
import json
from datetime import datetime, timezone

def datetime_converter(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")

load_dotenv()
url: str = os.environ.get("DATABASE_URL")
key: str = os.environ.get("DATABASE_API_SECRET")

supabase: Client = create_client(url, key)

class account:
    def __init__(self, user_id, accountType=None , accountNum = None):
        self._User_Id = user_id
        response = supabase.table("Accounts").select("*").eq("UserID" , user_id).eq("Account-Type" , accountType).eq("Account-Number", accountNum).execute()
        self.account_num = response.data[0]["Account-Number"]
        self.accountType = accountType
        self.balance = response.data[0]["Balance"]
        self.withdrawlim = response.data[0]["Withdraw-Limit"]
        self.dates = response.data[0]["Dates-Accessed"]
    def validate_string(self , input_val):
        if isinstance(input_val, str):
            return True
        else:
            return False
    def validate_int(self, input_val):
        if isinstance(input_val, int):
            return True
        else:
            return False
    def update_withdraw(self , new_withdraw):
        self.withdrawlim = new_withdraw
        response = supabase
    def add_bal(self, amount):
        if self.validate_int(amount):
            if amount > 0:
                self.balance += amount
                return {"Sucess": True}
            else:
                return {"Sucess": False}
        else:
            return {"Sucess": False}
    def remove_bal(self, amount):
        if self.validate_int(amount):
            if amount > 0 and self.balance > amount and amount < self.withdrawlim:
                self.balance -= amount
                return {"Sucess": True}
            else:
                return {"Sucess": False}
        else:
            return {"Sucess": False}
    def get_information(self):
        response = supabase.table("Accounts").select("*").eq("UserID" , self._User_Id).eq("Account-Type" , self.accountType).eq("Account-Number", self.account_num).execute()
        return response.data[0]
    def write_DB(self):
        now = datetime.now(timezone.utc).isoformat()
        self.dates.append(now)
        response = supabase.table("Accounts").update({"Dates-Accessed" : self.dates , "Balance": self.balance , "Withdraw-Limit": self.withdrawlim}).eq("Account-Type" , self.accountType).eq("UserID" , self._User_Id).eq("Account-Number" , self.account_num).execute()


'''
Testing
acct = account(user_id=12345678,accountNum= 7263, accountType="Checking")
print(acct.get_information())
print(acct.add_bal(600))
print(acct.remove_bal(90))
acct.update_withdraw(500)
print(acct.remove_bal(100))
acct.write_DB()
print(acct.get_information())
'''