from account import Account


class CheckingsAccount(Account):

    def __init__(self, first_name, last_name, account_type, account_balance):
        super().__init__(first_name, last_name, account_type, account_balance)