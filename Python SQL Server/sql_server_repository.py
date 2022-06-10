import pyodbc
from credential import Credential
from idatarepository import IDataRepository

class SqlServerRepository(IDataRepository):
    def add_credential(self, credential: Credential) -> None:
        conn = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', server='.', database='Credentials', trusted_connection='yes')

        cursor = conn.cursor()

        sql = 'INSERT INTO Credentials (UserName, [Password]) VALUES '
        sql += f' {credential.username}, {credential.password}'

        cursor.execute(sql)

    def get_credentials(self) -> list:
        conn = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', server='.', database='Credentials', trusted_connection='yes')

        cursor = conn.cursor()

        sql = 'SELECT Username, [Password] FROM Credentials '

        credentials = []

        for row in cursor.execute(sql):
            credentials.append(Credential(username=row.username, password=row.password))

        return credentials
    
    def get_credential(self, username: str) -> Credential:
        conn = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', server='.', database='Credentials', trusted_connection='yes')

        cursor = conn.cursor()

        sql = 'SELECT Username, [Password] FROM Credentials WHERE Username = ?;'

        parameters = [username]
        cursor.execute(sql, parameters) 
        row = cursor.fetchone()

        return Credential(username=row[0], password=row[1])

    def delete_credential(self, username: str) -> None:
        conn = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', server='.', database='Credentials', trusted_connection='yes')

        cursor = conn.cursor()

        sql = 'DELETE FROM Credentials WHERE Username = ?;'

        parameters = [username]

        cursor.execute(sql, parameters)

