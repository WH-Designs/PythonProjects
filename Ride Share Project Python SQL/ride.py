class ride:
    def __init__(self, riderid: int, ridestatus: bool, paymentstatus: bool, desiredpickuptime: str, pickuplocation: str, rideid=None, vehicleid=None, eta=None, destination=None):
        self._vehicleid = None
        self._riderid = riderid
        self._ridestatus = ridestatus
        self._paymentstatus = paymentstatus
        self._eta = None
        self._desiredpickuptime = desiredpickuptime
        self._destination = destination
        self._pickuplocation = pickuplocation
        self._driverid = None
        self._rideid = rideid

     
    def vehicleid(self):
        return self._vehicleid

     
    def riderid(self):
        return self._riderid

     
    def ridestatus(self):
        return self._ridestatus

     
    def paymentstatus(self):
        return self._paymentstatus

     
    def eta(self):
        return self._eta

     
    def desiredpickuptime(self):
        return self._desiredpickuptime

     
    def destination(self):
        return self._destination

     
    def pickuplocation(self):
        return self._pickuplocation

     
    def driverid(self):
        return self._driverid

     
    def rideid(self):
        return self._rideid

    
    def driverid(self, driver):
        self._driverid = driverid

    
    def vehicleid(self, vehicle):
        self._vehicleid = vehicleid

    
    def ridestatusid(self, ridestatus):
        self._ridestatus = ridestatus

    
    def paymentstatus(self, paymentstatus):
        self._paymentstatus = paymentstatus

    
    def eta(self, eta):
        self._eta = eta

    
    def rideid(self, rideid):
        self._rideid = rideid