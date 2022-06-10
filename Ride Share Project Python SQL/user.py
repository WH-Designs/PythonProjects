class user:
    def __init__(self, username: str, password: str, addressid: int, phone: str, email: str, balance: float, usertypeid: int, userid=None):
        self._userid = userid
        self._username = username
        self._password = password
        self._addressid = addressid
        self._phone = phone
        self._email = email
        self._balance = balance
        self._usertypeid = usertypeid
    
     
    def username(self):
        return self._username

     
    def password(self):
        return self._password

     
    def addressid(self):
        return self._addressid

     
    def phone(self):
        return self._phone

     
    def email(self):
        return self._email

     
    def balance(self):
        return self._balance

     
    def usertypeid(self):
        return self._usertypeid

     
    def userid(self):
        return self._userid

    
    def username(self, username):
        self._username = username


    def password(self, password):
        self._password = password

    
    def addressid(self, address):
        self._addressid = addressid

    
    def phone(self, phone):
        self._phone = phone


    def email(self, email):
        self._email = email

    def addToBalance(self, amount):
        self._balance += amount

    
    def userid(self, userid):
        self._userid = userid