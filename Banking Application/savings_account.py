from account import Account


class SavingsAccount(Account):

    def __init__(self, first_name, last_name, account_type, account_balance):
        super().__init__(first_name, last_name, account_type, account_balance)