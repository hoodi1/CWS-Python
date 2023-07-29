"""
Bank
    New object create (Constructor)
        amount=0
        account_no=randomly
        name=input
        bank_name

    Withdraw
    Deposit
    Display
    DisplayBalance
    Update
obj

"""
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
        print()
        print(f"------INFO------")
        print(f"Account Number = {self.accno}")
        print(f"Amount = {self.amount}")
        print(f"Name = {self.name}")
        print(f"Bank Name = {self.bankName}")
        print()

    def displayBalance(self):
        print()
        print(f"Your balance = {self.amount}")
        print()

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


accounts = []

def searchAccount(accountNumber):
    for i in accounts:
        if accountNumber == i.accno:
            return i
    else:
        return None

while True:
    print()
    print("1. Add account")
    print("2. Show all account")
    print("3. Search Account")
    print("4. Deposit")
    print("5. Withdraw")
    print("6. Check Balance")
    print("7. Transfer")
    print("8. Exit")
    print()
    choice = int(input("Enter your choice : "))

    if choice == 1:
        obj = Bank()
        accounts.append(obj)
        print(f"Account added. Your acc number is = {obj.accno}")
        print()
    elif choice == 2:
        if len(accounts) == 0:
            print("No accounts found")
        else:
            for i in accounts:
                i.display()
    elif choice == 3:
        acc_no = int(input("Enter account number : "))
        for i in accounts:
            if acc_no == i.accno: 
                i.display()
                break
        else:
            print("Account not found")
            print()
    
    elif choice == 4:
        acc_no = int(input("Enter account number : "))
        for i in accounts:
            if acc_no == i.accno: 
                i.deposit()
                break
        else:
            print("Account not found")
            print()

    elif choice == 5:
        acc_no = int(input("Enter account number : "))
        for i in accounts:
            if acc_no == i.accno: 
                i.withdraw()
                break
        else:
            print("Account not found")
            print()
    
    elif choice == 6:
        acc_no = int(input("Enter account number : "))
        result = searchAccount(acc_no)
        if result!=None:
            result.displayBalance()
        else:
            print("Account not found")
            print()

    elif choice == 7:
        acc_no = int(input("Enter your account number : "))
        senderAccount = searchAccount(acc_no)
        if senderAccount != None:
            rec_acc_no =  int(input("Enter reciever account number : ")) 
            reciverAccount = searchAccount(rec_acc_no)
            if reciverAccount != None:
                transferAmount = int(input("Enter Transfer amount : "))
                if transferAmount > senderAccount.amount:
                    print("You dont have enough balance")
                else:
                    senderAccount.amount -= transferAmount
                    reciverAccount.amount += transferAmount
                    print(f"Remaining Balance : {senderAccount.amount}")
            else:
                print("Reciever Account Not found!")
        else:
            print("Sender account does not exist")

    elif choice == 8:
        break