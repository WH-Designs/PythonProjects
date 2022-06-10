
# import pyodbc

# def connection_string() -> str:
#     driver = "{ODBC Driver 17 for SQL Server}"
#     server = "."  
#     database = "Library"  
#     username = "LPCordova"  
#     password = "xxxxxx"

#     return f'DRIVER={driver};SERVER={server};DATABASE={database};TRUST_CONNECTION=yes'

# #cnxn = connect(driver='{ODBC Driver 17 for SQL Server}', server='localhost', database='test', trusted_connection='yes')

# conn = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', server='.', database='Library', trusted_connection='yes')

# cursor = conn.cursor()

# category = input('Enter a category: ')
# parameters = [category]
# query = "SELECT BookId, Title, Author, Category from BOOK AS B WHERE B.CATEGORY=?"


# for row in cursor.execute(query, parameters):
#     print(row.BookId, row.Title, row.Author, row.Category)

from sql_server_repository import SqlServerRepository
from credential import Credential

def main():
    repo = SqlServerRepository()

    username = 'lucas' #input('Enter your username: ')
    password = 'Password1!' # input('Enter your password: ')

    credential: Credential = repo.get_credential(username)

    if password != credential.password:
        print(f'Access denied...')
    else:
        print(f'Access granted')


if __name__ == '__main__':
    main()





