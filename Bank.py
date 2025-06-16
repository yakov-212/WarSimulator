import random as rd
from datetime import datetime


class Transaction:
    def __init__(self, amount, transaction_type):
        self.date = datetime.now().strftime("%m/%d/%Y %H:%M")
        self.amount = amount
        self.transaction_type = transaction_type

    def __str__(self):
        return f"{self.date} - {self.transaction_type} - ${self.amount}"


class BankAccount:

    def __init__(self, name):
        self.name = name
        self.id = rd.randint(10000, 99999)
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{self.name} has successfully deposited ${amount}.")
            self.transactions.append(Transaction(amount, "Deposit"))
        else:
            print(f"{self.name}, You can't deposit an amount less than 0.")

    def withdraw(self, amount):
        if self.balance > 0:
            if 0 < amount < self.balance:
                self.balance -= amount
                print(f"{self.name} has successfully withdrawn ${amount}.")
                self.transactions.append(Transaction(amount, "withdrawn"))
            elif amount > self.balance:
                print(f"{self.name}, you only have ${self.balance} you cant withdraw ${amount}")
            else:
                print(f"{self.name}, you can't withdraw negative amount.")
        else:
            print(f"{self.name}, you have no money in your account to withdraw")

    def display_info(self):
        print(f"owner is {self.name}, your id is {self.id} and your balance is ${self.balance}")

    def print_transaction_history(self):
        print("...."*10)
        print("Transaction History:")
        for transaction in self.transactions:
            print(transaction)


class SavingsAccount(BankAccount):
    def __init__(self, name, minimum_balance):
        super().__init__(name)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print(f"{self.name} cannot withdraw {amount}, balance cannot go below {self.minimum_balance}")
        else:
            super().withdraw(amount)


class CheckingAccount(BankAccount):
    def __init__(self, name):
        super().__init__(name)
        self.has_checkbook = False

    def issue_checkbook(self):
        if not self.has_checkbook:
            self.has_checkbook = True
            print(f"{self.name} has been issued a checkbook.")
        else:
            print(f"{self.name} has already been issued a checkbook.")
