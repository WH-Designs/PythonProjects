class address:
    def __init__(self, line1: str, line2: str, zipid: int, localeid: int, addressid=None):
        self._line1 = line1
        self._line2 = line2
        self._zipid = zipid
        self._localeid = localeid
        self._addressid = addressid

     
    def line1(self):
        return self._line1

     
    def line2(self):
        return self._line2

     
    def zipid(self):
        return self._zipid

     
    def localeid(self):
        return self._localeid

     
    def addressid(self):
        return self._addressid

    
    def line1(self, line1):
        self._line1 = line1

    
    def line2(self, line2):
        self._line2 = line2

    
    def addressid(self, addressid):
        self.addressid = addressid