class vehicle:
    def __init__(self, licenseplate: int, makemodelid: int, vehicleid=None):
        self._licenseplate = licenseplate
        self._makemodelid = makemodelid
        self._vehicleid = vehicleid

     
    def licenseplate(self):
        return self._licenseplate

     
    def makemodelid(self):
        return self._makemodelid

     
    def vehicleid(self):
        return self._vehicleid

    
    def vehicleid(self, vehicleid):
        self._vehicleid = vehicleid