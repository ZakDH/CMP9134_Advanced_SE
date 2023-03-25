import random
from account import Account

class Bank:    
    def __init__(self):
        self.accounts = {}

    def createAccount(self, firstName, lastName):
        accountNumber = str(random.randint(100000, 999999))
        account = Account(firstName, lastName, accountNumber)
        self.accounts[accountNumber] = account
        print(f"Account created for {firstName} {lastName} with the account number {accountNumber}")

    def getAccount(self, accountNumber):
        return self.accounts.get(accountNumber)

    def viewDetails(self, accountNumber):
        account = self.accounts.get(accountNumber)
        if account:
            print(account)
        else:
            print("Account not found.")
    
    def transfer(self, accountNumberFrom, accountNumberTo, amount):
        accountFrom = self.getAccount(accountNumberFrom)
        accountTo = self.getAccount(accountNumberTo)
        if not accountFrom:
            print(f"Account {accountNumberFrom} not found.")
            return
        if not accountTo:
            print(f"Account {accountNumberTo} not found.")
            return
        try:
            accountFrom.withdraw(amount, accountFrom)
            accountTo.deposit(amount, accountTo)
        except ValueError as e:
            print(str(e))
    
    def listAccounts(self):
        if len(self.accounts) == 0:
            print("No accounts found.")
            return
        for account in self.accounts.values():
            print(f"{account.getOwnerName()}: {account.getAccountNumber()}, Balance: {account.checkBalance()}")

