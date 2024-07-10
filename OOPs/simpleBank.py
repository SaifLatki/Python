class Account:

    def __init__(self,balance,acc_no):
        self.balance = balance
        self.acc_no = acc_no

    def debit(self,amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Decreased balance by {amount}. New balance: {self.balance}")

    def credit(self, amount):
        self.balance += amount
        print(f"Increased balance by {amount}. New balance: {self.balance}")

    def display_balance(self):
        print(f"Account No: {self.acc_no}, Current Balance: {self.balance}")


acc1=Account(10000,123456)

acc1.display_balance()
acc1.debit(1000)
