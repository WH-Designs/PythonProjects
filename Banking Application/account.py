from abc import ABC


class Account(ABC):
    CHECKINGS = 1
    SAVINGS = 0

    def __init__(self, first_name, last_name, account_type, account_balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_type = account_type
        self.account_balance = account_balance
        self.account_status = 1

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_account_type(self):
        return self.account_type

    def get_account_balance(self):
        return self.account_balance

    def __eq__(self, other):
        return self.first_name == other.get_first_name() and \
            self.last_name == other.get_last_name() and \
            self.account_type == other.get_account_type()

    def __str__(self):
        return f'{self.account_type}: {self.first_name}, {self.last_name}, {self.account_balance}'