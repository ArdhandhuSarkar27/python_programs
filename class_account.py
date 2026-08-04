class Account:
    def __init__(self, balance, account):
        self.balance = balance
        self.account_number = account

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "has been debited from your account.")
        print("Total balance =",self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "has been credited to your account.")
        print("Total balance =", self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Account(10000, 123456)
acc1.credit(500)
acc1.debit(2000)
print("Final balance =", acc1.get_balance())

        