class usertype:
    def __init__(self, usertypeid: int, type: str):
        self._usertypeid = usertypeid
        self._type = type

     
    def usertypeid(self):
        return self._usertypeid

     
    def type(self):
        return self._type


