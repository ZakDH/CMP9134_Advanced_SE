import random

class Account:
    def __init__(self, accountNumber, balance=0):
        self.__accountNumber = accountNumber
        self.__balance = balance

    def getAccountNumber(self):
        return self.__accountNumber

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposit of {amount} was successful. New balance: {self.__balance}")

    def checkBalance(self):
        return self.__balance
    
    def withdraw(self, amount):
        if self.__balance < amount:
            raise ValueError(f"Withdrawal of {amount} failed. Insufficient funds.")
        self.__balance -= amount
        print(f"Withdrawal of {amount} was successful. New balance: {self.__balance}")
    
    def transfer(self, amount, recipient):
        if self.__balance >= amount:
            self.__balance -= amount
            recipient.deposit(amount)
            print(f"Transfer of {amount} was successful. New balance: {self.__balance}")
        else:
            print(f"Transfer of {amount} failed. Insufficient funds.")

    def __str__(self):
        return f"Account Number: {self.__accountNumber}, Balance: {self.__balance}"

class Bank:    
    def __init__(self):
        self.__accounts = {}

    def createAccount(self, firstName, lastName):
        accountNumber = str(random.randint(100000, 999999))
        self.__accounts[accountNumber] = Account(accountNumber)
        print(f"Account created for {firstName} {lastName} with the account number {accountNumber}")

    def getAccount(self, accountNumber):
        return self.__accounts.get(accountNumber)

    def viewDetails(self, accountNumber):
        account = self.__accounts.get(accountNumber)
        if account:
            print(account)
        else:
            print("Account not found.")

bank = Bank()
while True:
    print("What service do you wish to use?")
    print("1. Create an account")
    print("2. Deposit into account")
    print("3. Withdraw from account")
    print("4. Transfer between accounts")
    print("5. View account details")
    print("6. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        firstName = input("What is your first name?: ")
        lastName = input("What is your last name?: ")
        bank.createAccount(firstName, lastName)
            
    elif choice == "2":
        accountNumber = input("Enter account number: ")
        account = bank.getAccount(accountNumber)
        if account:
            depositAmount = float(input("Please enter deposit amount:" ))
            account.deposit(depositAmount)
        else:
            print("Account has not been found...")
            
    elif choice == "3":
        accountNumber = input("Enter account number: ")
        account = bank.getAccount(accountNumber)
        if account:
            withdrawAmount = float(input("Please enter withdrawal amount:" ))
            account.withdraw(withdrawAmount)
        else:
            print("Account has not been found...")

    elif choice == "4":
        accountFrom = input("Enter the account number you want to transfer funds from: ")
        accountFrom = bank.getAccount(accountFrom)
        if accountFrom:
            accountTo = input("Enter the account number you want to transfer funds to: ")
            accountTo = bank.getAccount(accountTo)
            if accountTo:
                amount = float(input("Enter amount to transfer: "))
                accountFrom.transfer(amount, accountTo)
            else:
                print("Recipient account has not been found...")
        else:
            print("Account has not been found...")
    
    elif choice == "5":
        accountNumber = input("Enter account number: ")
        bank.viewDetails(accountNumber)

    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid choice.")