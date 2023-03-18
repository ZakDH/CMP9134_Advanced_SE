import random

class Account:
    def __init__(self, account_number, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def checkBalance(self):
        return self.__balance

def createAccount(name):
    account_number = str(random.randint(100000, 999999))
    account = Account(account_number)
    print(f"Account created for {name} with the account number {account_number}")
    return account


# Example usage
name = input("What is your first name?: ")
account = createAccount(name)
deposit = input("How much do you want to deposit into your new account?: ")
deposit = int(deposit)
account.deposit(deposit)
print(account.checkBalance())