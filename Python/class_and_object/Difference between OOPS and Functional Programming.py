# 1. Object-Oriented Programming (OOP) in Python
# Definition: 
# OOP is a paradigm that bundles data (attributes) and behavior (methods) together into a single unit called an Object. It relies on modifying the internal state of that object.
# Python Example:
class Bankaccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient balance")
        else:
            self.balance-=amount
    def display_balance(self):
        print(f"Account Number: {self.account_number}, Account Holder: {self.account_holder}, Balance: {self.balance}")
customer1=Bankaccount("1234567890","John Doe",1000)
customer1.deposit(500)
customer1.display_balance()
customer1.withdraw(200)
customer1.display_balance()
