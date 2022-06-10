class makemodel:
    def __init__(self, make: str, model: str, makemodelid=None):
        self._makemodelid = makemodelid
        self._make = make
        self._model = model

     
    def makemodelid(self):
        return self._makemodelid

     
    def make(self):
        return self._make

     
    def model(self):
        return self._model

    
    def makemodelid(self, makemodelid):
        self._makemodelid = makemodelid


