class Credential:
    def __init__(self, username: str, password: str) -> None:
        self._username = username
        self._password = password
    
    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @username.setter
    def username(self, username):
        self._username = username
    
    @password.setter
    def password(self, password):
        self._password = password
