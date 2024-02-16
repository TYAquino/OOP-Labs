'''
file: Bank-Acc-Class.py
Author: Trisha Aquino
Description: A lab classes and objects assignment in Object-Oriented course
Version: Dec. 3, 2023
'''

# Turning the Bank Account class into private so it's more secure
class BankAccount:
    def __init__(self, accountNumber, customerName, balance):
        self.__accountNumber = accountNumber
        self.__customerName = customerName
        self.__balance = balance

    def get_accountNumber(self):
        return self.__accountNumber
    
    def get_customerName(self):
        return self.__customerName

    def get_balance(self):
        return self.__balance
    
    def set_customerName(self, customerName):
        self.__customerName = customerName

    def set_balance(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return self.__balance
        else:
            return 'Please enter valid amount...'
    
    def withdraw(self, amount):
        if amount > self.__balance:
            return 'Insufficient funds...'
        else:
            self.__balance -= amount
            return self.__balance
        
    def display(self):
        return self.__balance

# Ask the user's input for details
accountNumber = input("Enter account number: ")
customerNumber = input("Enter customer number: ")
balance = float(input("Enter account balance: "))

# Creating new bank account
new_account = BankAccount(accountNumber, customerNumber, balance)

# Deposit the user's money into the bank account
amount = float(input("Enter deposit amount: "))
print(new_account.deposit(amount))

# Withdraw money from the bank account
amount = float(input("Enter withdraw amount: "))
print(new_account.withdraw(amount))

# Display the account balance
print(f'Account balance: {new_account.display()}')