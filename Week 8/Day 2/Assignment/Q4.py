'''Write a Python class named BankAccount with a constructor
that takes no arguments and prompts the user for an initial
balance and an account number. The constructor should initialize
two instance variables, balance and accountNumber. Write
methods named deposit and withdraw that allow the user to
deposit or withdraw money from the account.'''

import random

class Bank:
    """this class is used to creat a bank"""
    def __init__(self):
        self.amount = 0
        self.accno = random.randint(100000, 999999)
        self.name = input("Enter name : ")
        self.bankName = input("Enter Bank name : ")

    def __str__(self):
        return "You have printed an object directly"

    def display(self):
        print(f"------INFO------")
        print(f"Account Number = {self.accno}")
        print(f"Amount = {self.amount}")
        print(f"Name = {self.name}")
        print(f"Bank Name = {self.bankName}")

    def displayBalance(self):
        print(f"Your balance = {self.amount}")

    def deposit(self):
        """this method is used to deposit a bank"""
        newAmmount = int(input("Enter amount to deposit = "))
        self.amount = self.amount + newAmmount
        self.displayBalance()

    def withdraw(self):
        newAmount = int(input("Enter amount to withdraw = "))
        if newAmount > self.amount:
            print(f"Infsuficient Balance = {self.amount}")
        else:
            self.amount = self.amount - newAmount
            print(f"Withdraw amount = {newAmount}")
            self.displayBalance()

    def update(self):
        print()
        name = input("Enter name (Leave blank if you dont want to change)")
        bank_name = input("Enter Bank Name (Leave blank if you dont want to change)")
        if name:
            self.name = name
        if bank_name:
            self.bankName = bank_name



obj = Bank()
obj.deposit()
obj.display()
obj.withdraw()
obj.update()
obj.display()

print(Bank.__doc__)
print(Bank.deposit.__doc__)
