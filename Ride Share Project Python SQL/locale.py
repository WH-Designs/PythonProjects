class locale:
    def __init__(self, city: str, state: str, localeid=None):
        self._city = city
        self._state = state
        self._localeid = localeid

     
    def city(self):
        return self.city

     
    def state(self):
        return self._state

     
    def localeid(self):
        return self._localeid

    
    def localeid(self, localeid):
        self._localid = localeid