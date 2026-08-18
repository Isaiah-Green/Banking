import random
from Account import account
class Customer:
    def __init__(self , username, password):
        self._User_Name = username
        self._Password = password
        self._User_ID = random.randint(100000000 , 999999999)
        self.credit_borrow = 0.0
        self.credit_score = 0
        self._accounts = []
    ####Functions that All Users will have access to
    def me(self):
        pass
    