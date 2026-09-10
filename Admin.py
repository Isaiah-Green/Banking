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

class Admin:
    def __init__(self , userName = None, password = None, AdminID= None , newAdmin = 0):
        self.userName = userName
        self.password = password
        self.AdminID = AdminID
        self.total_in_acc = 0.0
        self.total_credit = 0.0
        self.last_updated = []
        self.last_updated.append(datetime.now(timezone.utc).isoformat())
        self.new_Admin_entry(newAdmin)
    def load_admin(self, userName, password):
        response = supabase.table("Admin").select("*").eq("UserName" , userName).eq("Password" , password).execute()
        self.userName = response.data[0]["UserName"]
        self.password = response.data[0]["Password"]
        self.AdminID = response.data[0]["AdminID"]
        self.total_in_acc = response.data[0]["Total-in-Bank"]
        self.total_credit = response.data[0]["Total-Credit"]
        self.last_updated = response.data[0]["Last-Updated"]
    def new_Admin_entry(self , int):
        if int > 0:
            supabase.table("Admin").insert({
                "UserName": self.userName,
                "Password": self.password,
                "AdminID": self.AdminID,
                "Total-in-Bank": self.total_in_acc,
                "Total-Credit": self.total_credit,
                "Last-Updated": self.last_updated}
            ).execute()
    def See_DB_customer(self):
        response = supabase.table("Customer-List").select("*").execute()
        return response.data
    #function to see entire Customer Account FIle
    def See_DB_account(self):
        response = supabase.table("Accounts").select("*").execute()
        return response.data
    #function to see current amount in bank
    def total_in_bank(self):
        total = 0.0
        response = supabase.table("Accounts").select("*").eq("Account-Type" , "Checking").eq("Account-Type" , "Savings").execute()
        for item in response.data:
            total += item["Balance"]
        self.total_in_acc = total
        return self.total_in_acc
    #function to see current aount of credit loaned out
    def total_credit_lent(self):
        total = 0.0
        response = supabase.table("Accounts").select("*").eq("Account-Type" , "Credit").execute()
        for item in response.data:
            total += item["Balance"]
        self.total_credit = total
        return self.total_credit
    def get_last_total_in_bank(self):
        return self.total_in_acc
    def get_last_total_credit(self):
        return self.total_credit
    #function to enter a userID and pull up all accounts associated with them and their customer function entry
    def lookup_user(self , userID):
        response = supabase.table("Customer-List").select("*").eq("UserID" , userID).execute()
        response2 = supabase.table("Accounts").select("*").eq("UserID", userID).execute()
        return {"Customer": response.data[0] , "Accounts": response2.data}    
    #function to reset credentials for admin
    def reset_password(self, userName, AdminID , new_password):
        response = supabase.table("Admin").update({"Password" : new_password}).eq("UserName" , userName).eq("AdminID" , AdminID).execute()
    #function to cloes accounts
    def close_all_accounts(self, userID):
        response = supabase.table("Accounts").delete().eq("UserID" , self._User_ID).execute()
    def close_one_account(self,userID, accNum):
        response = supabase.table("Accounts").delete().eq("UserID" , self._User_ID).eq("Account-Number", accNum).execute()
    def close_customer(self, userID):
        response = supabase.table("Customer-List").delete().eq("UserID", userID).execute()
    def write_admin(self):
        now = datetime.now(timezone.utc).isoformat()
        self.last_updated.append(now)
        response = supabase.table("Admin").update({"Last-Updated" : self.last_updated , "Total-in-Bank": self.total_in_acc , "Total-Credit":self.total_credit}).eq("UserName" , self.userName).eq("Password" , self.password).execute()

'''
Testing
admin = Admin("Ilikethegreens" , "ihategreens3232" , 7869 , 1)
print(admin.See_DB_account())
print(admin.total_in_bank())
admin.close_customer(12345678)
print(admin.total_credit_lent())
admin.reset_password("Ilikethegreens" , 7869 , "Iamtheonly6767")
admin.write_admin()
'''