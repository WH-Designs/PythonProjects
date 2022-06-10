import csv
from checkings_account import CheckingsAccount
from savings_account import SavingsAccount
import matplotlib.pyplot as plt
import numpy as np


class Bank:

    def __init__(self, checkings_file, savings_file):
        self.checkings_accounts = []
        self.savings_accounts = []
        self.checkings_file = checkings_file
        self.savings_file = savings_file
        self.load_checkings_data()
        self.load_savings_data()

    def load_checkings_data(self):
        self.checkings_accounts.clear()
        with open(self.checkings_file) as file:
            for item in csv.reader(file, delimiter=',', skipinitialspace=True):
                self.checkings_accounts.append(CheckingsAccount(item[0], item[1], item[2], item[3]))

    def load_savings_data(self):
        self.savings_accounts.clear()
        with open(self.savings_file) as file:
            for item in csv.reader(file, delimiter=',', skipinitialspace=True):
                self.savings_accounts.append(SavingsAccount(item[0], item[1], item[2], item[3]))

    def save_checkings_account(self):
        with open(self.checkings_file, 'w') as file:
            for account in self.checkings_accounts:
                file.write(
                    f'{account.get_first_name()}, {account.get_last_name()}, {account.get_account_type()}, {account.get_account_balance()}\n')

    def save_savings_account(self):
        with open(self.savings_file, 'w') as file:
            for account in self.savings_accounts:
                file.write(
                    f'{account.get_first_name()}, {account.get_last_name()}, {account.get_account_type()}, {account.get_account_balance()}\n')

    def create_account(self, account):
        if account.account_status == 1:
            if account.get_account_type() == 1:
                self.checkings_accounts.append(account)
                self.save_checkings_account()
            else:
                self.savings_accounts.append(account)
                self.save_savings_account()
        else:
            print('Account is closed')

    def find_account_by_last_name(self, last_name, account_type):
        if account_type == 1:
            for account in self.checkings_accounts:
                if last_name == account.get_last_name():
                    return account
        else:
            for account in self.savings_accounts:
                if last_name == account.get_last_name():
                    return account

    def close_account(self, account):
        if int(account.account_status) == 1:
            account.account_status = 0
        else:
            print('Account already closed')

    def deposit_money(self, account, amount):
        if int(account.get_account_type()) == 1:
            for account1 in self.checkings_accounts:
                if account == account1:
                    account1.account_balance = float(account1.account_balance) + amount
                    self.save_checkings_account()
        else:
            for account1 in self.savings_accounts:
                if account == account1:
                    account1.account_balance = float(account1.account_balance) + amount
                    self.save_savings_account()

    def withdraw_money(self, account, amount):
        if int(account.get_account_type()) == 1:
            for account1 in self.checkings_accounts:
                if account == account1:
                    account1.account_balance = float(account1.account_balance) - amount
                    self.save_checkings_account()
        else:
            for account1 in self.savings_accounts:
                if account == account1:
                    account1.account_balance = float(account1.account_balance) - amount
                    self.save_savings_account()

    def print_plot(self):

        total_checking = 0
        total_savings = 0

        for account in self.checkings_accounts:
            total_checking += float(account.get_account_balance())
        for account in self.savings_accounts:
            total_savings += float(account.get_account_balance())

        objects = ('Checking', 'Savings')
        y_pos = np.arange(len(objects))
        y_values = [int(total_checking), int(total_savings)]

        plt.bar(y_pos, y_values, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('Amount of money in total')
        plt.title('Total Money in Checking and Savings Accounts')

        plt.show()