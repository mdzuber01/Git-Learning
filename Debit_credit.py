class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc
        print(f"Initial abalance in your account is : {bal}")
    def debit(self,amount):
        self.balance-=amount
        print(f" Your NRS {amount} has been debited")
        print(f"Total available balance = {self.get_balance()}")
    def credit(self,amount):
        self.balance+=amount
        print(f" Your NRS {amount} has been Credited")
        print(f"Total available balance = {self.get_balance()}")
    def get_balance(self):
        return self.balance
ac1=Account(10000,123)
#ac1.debit(1000)
ac1.credit(2000) 
ac1.credit(23044)

