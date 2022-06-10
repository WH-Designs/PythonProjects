class zip:
    def __init__(self, code: int, zipid=None):
        self._code = code
        self._zipid = zipid

     
    def code(self):
        return self._code

     
    def zipid(self):
        return self.zipid

    
    def zipid(self, zipid):
        self._zipid = zipid


