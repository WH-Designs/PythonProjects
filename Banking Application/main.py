from bank import Bank
from account import Account
from checkings_account import CheckingsAccount
from savings_account import SavingsAccount




def main():

    menu = '1. Open an Account\n2. Close an Account\n3. Withdraw\n4. Deposit\n5. Plot Accounts Amounts\n6. Quit'

    choice = int(input(menu + '\n--> '))

    bank = Bank('checkings.csv', 'savings.csv')

    while choice != 6:
        if choice == 1:
            # Open an Account
            first_name = input('Enter a first name: ')
            last_name = input('Enter a last name: ')
            account_type = int(input('Enter the account type (1) Checkings (0) Savings: '))

            if account_type == Account.CHECKINGS:
                account = CheckingsAccount(first_name, last_name, Account.CHECKINGS, 0)
            else:
                account = SavingsAccount(first_name, last_name, Account.SAVINGS, 0)

            bank.create_account(account)

        elif choice == 2:
            # Close an Account
            last_name = input('Enter the last name of the account: ')
            account_type = int(input('Enter the account type (1) Checkings (0) Savings: '))

            try:
                account = bank.find_account_by_last_name(last_name, account_type)
                bank.close_account(account)
            except Exception as exception:
                print(f'Account with last name {last_name} not found. Try again.')

        elif choice == 3:
            # Withdraw money
            last_name = input('Enter the last name of the account: ')
            account_type = int(input('Enter the account type (1) Checkings (0) Savings: '))
            amount = float(input('Enter the amount you want to Withdraw: '))
            account = bank.find_account_by_last_name(last_name, account_type)
            bank.withdraw_money(account, amount)
            print(account)

        elif choice == 4:
            # Deposit money
            last_name = input('Enter the last name of the account: ')
            account_type = int(input('Enter the account type (1) Checkings (0) Savings: '))
            amount = float(input('Enter the amount you want to Deposit: '))
            account = bank.find_account_by_last_name(last_name, account_type)
            bank.deposit_money(account, amount)
            print(account)
        elif choice == 5:
            bank.print_plot()
        else:
            print('Invalid option')

        choice = int(input(menu + '\n--> '))





if __name__ == '__main__':
    main()
