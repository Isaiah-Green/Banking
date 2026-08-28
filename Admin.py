import datetime

class Admin:
    def __init__(self , userName, password, AdminID , cus_file, acc_file , admin_file):
        self.userName = userName
        self.password = password
        self.AdminID = AdminID
        self.cus_file = cus_file
        self.admin_file = admin_file
        self.acc_file = acc_file
        self.total_in_acc = 0.0
        self.total_credit = 0.0
        self.last_updated = datetime.datetime.now()
    #function to see entire Cutomer DB file
    #format = [UserName:  , Password: , AdminID: , Customer FIle: , acc_file:  , admin File:  , total: , total credit: , last updated:  , refresh: ](temporary to store the files once DB is properly made wont save 3 diff ones just one big one)
    def load_admin(self, userName, password , AdminID , admin_file):
        try:
            with open(admin_file , "r") as f:
                for line in f:
                    y = line.split(" ")
                    if y[1] == userName and y[4] == password and y[7] == AdminID:
                        self.userName = userName
                        self.password = password
                        self.AdminID = AdminID
                        self.cus_file = y[11]
                        self.acc_file = y[14]
                        self.admin_file = y[18]
                        self.total_credit = y[25]
                        self. total_in_bank = y[21]
                        self.last_updated = y[29]
                        return {"Sucess" : True}
        except FileNotFoundError:
            print("Error: The file does not exist.")
            return{"Sucess" : False}
    def See_DB_customer(self):
        try:
            with open(self.cus_file, "r") as f:
                for line in f:
                    print(line)
                return {"Sucess" : True}
        except:
            return {"Sucess" : False}
    #function to see entire Customer Account FIle
    def See_DB_account(self):
        try:
            with open(self.acc_file, "r") as f:
                for line in f:
                    print(line)
                return {"Sucess" : True}
        except:
                    return {"Sucess" : False}
    #function to see current amount in bank
    def total_in_bank(self):
        temp = 0
        try:
            with open(self.acc_file, "r") as f:
                for line in f:
                    y = line.split(" ")
                    if y[9] == "Savings" or y[9] == "Checking":
                        y = line.split(" ")
                        temp += int(y[12])
                self.total_in_acc = temp
                return {"Sucess" : True , "Total" : self.total_in_acc}
        except FileNotFoundError:
            return {"Sucess" : False}
    #function to see current aount of credit loaned out
    def total_credit_lent(self):
            temp = 0
            try:
                with open(self.acc_file, "r") as f:
                    for line in f:
                        y = line.split(" ")
                        if y[9] == "Credit":
                            y = line.split(" ")
                            temp += int(y[12])
                    self.total_credit = temp
                    return {"Sucess" : True , "Total" : self.total_credit}
            except FileNotFoundError:
                return {"Sucess" : False}
    def get_last_total_in_bank(self):
        return self.total_in_acc
    def get_last_total_credit(self):
        return self.total_credit
    #function to enter a userID and pull up all accounts associated with them and their customer function entry
    def lookup_user(self , userID):
        try:
            with open(self.cus_file , "r") as f:
                for line in f:
                    y = line.split(" ")
                    if y[1] == str(userID):
                        print(line)
                try:
                    with open(self.acc_file, "r") as f:
                        for line in f:
                            y = line.split(" ")
                            if y[1] == str(userID):
                                print(line)
                        return {"Sucess" : True}
                except FileNotFoundError:
                    return {"Sucess" : False}
        except FileNotFoundError:
            return {"Sucess" : False}
    #write to DB
    def write_admin(self):
        try:
            with open(self.admin_file, "r") as f:
                for line in f:
                    y = line.split(" ")
                    if y[1] == self.userName and y[4] == self.password and y[7] == self.AdminID:
                        return {"Sucess" : True}
                with open(self.admin_file, "w" , encoding= 'utf=8') as f:
                    f.write(f"[UserName: {self.userName} , Password: {self.password} , AdminID: {self.AdminID} , Customer FIle: {self.cus_file}, acc_file: {self.acc_file}  , admin File: {self.admin_file} , total: {self.total_in_acc} , total credit: {self.total_credit} , last updated: {self.last_updated}]")
                    return {"Sucess": True}
        except:
            return {"Sucess": False}
    #function to reset credentials for himself(maybe)
    def reset_password(self, userName, AdminID):
        pass
    #function to cloes accounts
    def close_accounts(self, userID):
        try: 
            with open(self.acc_file,"r+") as f:
                    new_f = f.readlines()
                    f.seek(0)
                    for line in new_f:
                        y = line.split(" ")
                        if not y[1] == str(userID):
                            f.write(line)
                    f.truncate()
                    return {"Sucess" : True}
        except:
            return {"Sucess": False}
    def close_customer(self, userID):
        try: 
            with open(self.cus_file,"r+") as f:
                new_f = f.readlines()
                f.seek(0)
                for line in new_f:
                    y = line.split(" ")
                    if  not y[1] == str(userID):
                        f.write(line)
                f.truncate()
                t = self.close_accounts(userID)
                if t["Sucess"]:
                    return {"Sucess" : True}
        except:
            return {"Sucess": False}

'''
Testing
'''
admin = Admin("ilikegrapes0" , "ihategrapes0" , 1234 , "customer_testing.txt" , "testing_account.txt" , "aadmin_testing.txt")
admin.See_DB_customer()
print(admin.write_admin())
print("---------------------------------------------")
admin.See_DB_account()
print(admin.total_credit_lent())
print(admin.total_in_bank())
print("---------------------------------------------")
admin.lookup_user(876546756)
print(admin.close_customer(876546756))
print("---------------------------------------------")
admin.See_DB_customer()
print("---------------------------------------------")
admin.See_DB_account()
