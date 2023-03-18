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