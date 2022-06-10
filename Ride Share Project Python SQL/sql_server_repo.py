import pyodbc
from datarepository import datarepository
from zip import zip
from locale import locale
from address import address
from vehicle import vehicle
from ride import ride
from user import user
from usertype import usertype
from makemodel import makemodel

class SqlServerRepository(datarepository):
    def add_user(self, user: user) -> None:
        connection = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', server='.', database='RideShare', trusted_connection='yes')

        cursor = connection.cursor()

        sql = 'INSERT INTO [User] (UserTypeId, UserName, [Password], AddressId, UserPhone, UserEmail) VALUES '
        sql += f' ({user.usertype}, {user.username}, {user.password}, {user.address}, {user.phone}, {user.email})'

        cursor.execute(sql)

    
    def get_user(self, username: str) -> user:
        connection = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', server='.', database='RideShare', trusted_connection='yes')

        cursor = connection.cursor()

        sql = 'SELECT UserId, UserTypeId, UserName, [Password], AddressId, UserPhone, UserEmail, UserBalance FROM [User] WHERE UserName = ?;'

        parameters = [username]
        cursor.execute(sql, parameters)
        row = cursor.fetchone()

        return user(username=row[2], password=row[3], addressid=row[4], phone=row[5], email=row[6], balance=row[7], usertypeid=row[1], userid=row[0])

    
    def delete_user(self, username: str) -> None:
        connection = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', server='.', database='RideShare', trusted_connection='yes')

        cursor = connection.cursor()

        sql = 'DELETE FROM [User] WHERE UserName = ?;'

        parameters = [username]

        cursor.execute(sql, parameters)

 
    def get_users(self) -> list:
        connection = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', server='.', database='RideShare', trusted_connection='yes')

        cursor = connection.cursor()

        sql = 'SELECT UserId, UserTypeId, UserName, [Password], AddressId, UserPhone, UserEmail, UserBalance FROM [User] '

        users = []

        for row in cursor.execute(sql):
            users.append(user(username=row[2], password=row[3], addressid=row[4], phone=row[5], email=row[6], balance=row[7], usertypeid=row[1], userid=row[0]))

        return users
    

    def add_ride(self, ride: ride) -> None:
        connection = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', server='.', database='RideShare', trusted_connection='yes')

        cursor = connection.cursor()

        sql = 'INSERT INTO Ride (VehicleId, UserId, User2Id, RideStatus, PaymentStatus, ETA, PickupTime, Destination, PickupLocation) VALUES '
        sql += f' ({ride.riderid}, {ride.driverid}, {ride.ridestatus}, {ride.paymentstatus}, {ride.desiredpickuptime}, {ride.pickuplocation}, {ride.vehicleid}, {ride.eta}, {ride.destination}) '

        cursor.execute(sql)

    
    def get_ride(self, rideid: int) -> ride:
        connection = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', server='.', database='RideShare', trusted_connection='yes')

        cursor = connection.cursor()

        sql = 'SELECT (RideId, VehicleId, UserId, User2Id, RideStatus, PaymentStatus, ETA, PickupTime, Destination, PickupLocation) FROM Ride WHERE RideId = ?;'

        parameters = [userid]
        cursor.execute(sql, parameters)
        row = cursor.fetchone()

        return ride(riderid=row[2], ridestatus=row[4], paymentstatus=row[5], desiredpickuptime=row[7], pickuplocation=row[9], driverid=row[3], rideid=row[0], vehicleid=row[1], eta=row[6], destination=row[8])

    
    def get_rides(self) -> list:
        connection = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', server='.', database='RideShare', trusted_connection='yes')

        cursor = connection.cursor()

        sql = 'SELECT RideId, VehicleId, UserId, User2Id, RideStatus, PaymentStatus, ETA, PickupTime, Destination, PickupLocation FROM Ride '

        rides = []

        for row in cursor.execute(sql):
            rides.append(ride(riderid=row[2], ridestatus=row[4], paymentstatus=row[5], desiredpickuptime=row[7], pickuplocation=row[9], driverid=row[3], rideid=row[0], vehicleid=row[1], eta=row[6], destination=row[8]))

        return rides

    
    def delete_ride(self, rideid: int) -> None:
        connection = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', server='.', database='RideShare', trusted_connection='yes')

        cursor = connection.cursor()

        sql = 'DELETE FROM Ride WHERE RideId = ?;'

        parameters = [rideid]

        cursor.execute(sql, parameters)

    
    def add_vehicle(self, vehicle: vehicle) -> None:
        connection = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', server='.', database='RideShare', trusted_connection='yes')

        cursor = connection.cursor()

        sql = 'INSERT INTO Vehicle (MakeModelId, VehicleLicensePlate) VALUES '
        sql += f' ({vehicle.makemodelid}, {vehicle.licenseplate})'

        cursor.execute(sql)

    
    def delete_vehicle(self, vehicleid: int) -> None:
        connection = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', server='.', database='RideShare', trusted_connection='yes')

        cursor = connection.cursor()

        sql = 'DELETE FROM Vehicle WHERE VehicleId = ?;'

        parameters = [vehicleid]

        cursor.execute(sql, parameters)

    
    def get_vehicle(self, vehicleid: int) -> vehicle:
        connection = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', server='.', database='RideShare', trusted_connection='yes')

        cursor = connection.cursor()

        sql = 'SELECT (VehicleId, MakeModelId, VehicleLicensePlate) FROM Vehicle WHERE VehicleId = ?;'

        parameters = [vehicleid]
        cursor.execute(sql, parameters)
        row = cursor.fetchone()

        return vehicle(makemodelid=row[1], licenseplate=row[2], vehicleid=row[0])

    
    def get_address(self, addressid: int) -> address:
        connection = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', server='.', database='RideShare', trusted_connection='yes')

        cursor = connection.cursor()

        sql = 'SELECT (AddressId, Line1, Line2, ZipId, LocaleId) FROM [Address] WHERE AddressId = ?;'

        parameters = [addressid]
        cursor.execute(sql, parameters)
        row = cursor.fetchone()

        return address(line1=row[1], line2=row[2], zipid=row[3], localeid=row[4], addressid=row[0])

    
    def add_address(self, address: address) -> None:
        connection = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', server='.', database='RideShare', trusted_connection='yes')

        cursor = connection.cursor()

        sql = 'INSERT INTO [Address] (Line1, Line2, ZipId, LocaleId) VALUES '
        sql += f' ({address.line1}, {address.line2}, {address.zipid}, {address.localeid})'

        cursor.execute(sql)

    
    def get_zip(self, zipid: int) -> zip:
        connection = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', server='.', database='RideShare', trusted_connection='yes')

        cursor = connection.cursor()

        sql = 'SELECT (ZipId, Code) FROM Zip WHERE ZipId = ?;'

        parameters = [zipid]
        cursor.execute(sql, parameters)
        row = cursor.fetchone()

        return zip(code=row[1], zipid=row[0])

    
    def add_zip(self, zip: zip) -> None:
        connection = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', server='.', database='RideShare', trusted_connection='yes')

        cursor = connection.cursor()

        sql = 'INSERT INTO Zip (Code) VALUES'
        sql += f' ({zip.code})'

        cursor.execute(sql)

    
    def get_locale(self, localeid: int) -> locale:
        connection = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', server='.', database='RideShare', trusted_connection='yes')

        cursor = connection.cursor()

        sql = 'SELECT (LocaleId, City, [State]) FROM Locale WHERE LocaleId = ?;'

        parameters = [localeid]
        cursor.execute(sql, parameters)
        row = cursor.fetchone()

        return locale(city=row[1], state=row[2], localeid=row[0])

    
    def add_locale(self, locale: locale) -> None:
        connection = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', server='.', database='RideShare', trusted_connection='yes')

        cursor = connection.cursor()

        sql = 'INSERT INTO Locale (City, [State]) VALUES '
        sql += f' ({locale.city}, {locale.state})'

        cursor.execute(sql)


    def get_usertype(self, usertypeid: int) -> usertype:
        connection = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', server='.', database='RideShare', trusted_connection='yes')

        cursor = connection.cursor()

        sql = 'SELECT (UserTypeId, UserType) FROM UserTypes WHERE UserTypeId = ?;'

        parameters = [usertypeid]
        cursor.execute(sql, parameters)
        row = cursor.fetchone()

        return usertype(usertypeid=row[0], type=row[1])


    def get_usertypes(self) -> list:
        connection = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', server='.', database='RideShare', trusted_connection='yes')

        cursor = connection.cursor()

        sql = 'SELECT UserTypeId, UserType FROM UserTypes'

        usertypes = []

        for row in cursor.execute(sql):
            usertypes.append(usertype(usertypeid=row[0], type=row[1]))

        return usertypes


    def get_makemodel(self, makemodelid) -> makemodel:
        connection = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', server='.', database='RideShare', trusted_connection='yes')

        cursor = connection.cursor()

        sql = 'SELECT (MakeModelId, Make, Model) FROM MakeModel WHERE MakeModelId = ?;'

        parameters = [makemodelid]
        cursor.execute(sql, parameters)
        row = cursor.fetchone()

        return makemodel(make=row[1], model=row[2], makemodelid=row[0])


    def add_makemodel(self, makemodel: makemodel) -> None:
        connection = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', server='.', database='RideShare', trusted_connection='yes')

        cursor = connection.cursor()

        sql = 'INSERT INTO MakeModel (Make, Model) VALUES '
        sql += f' ({makemodel.make}, {makemodel.model})'

        cursor.execute(sql)


    def get_zips(self) -> list:
        connection = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', server='.', database='RideShare', trusted_connection='yes')

        cursor = connection.cursor()

        sql = 'SELECT ZipId, Code FROM Zip'

        zips = []

        for row in cursor.execute(sql):
            zips.append(zip(code=row[1], zipid=row[0]))

        return zips


    def get_locales(self) -> list:
        connection = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', server='.', database='RideShare', trusted_connection='yes')

        cursor = connection.cursor()

        sql = 'SELECT LocaleId, City, [State] FROM Locale'

        locales = []

        for row in cursor.execute(sql):
            locales.append(locale(city=row[1], state=row[2], localeid=row[0]))

        return locales


    def get_addresses(self) -> list:
        connection = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', server='.', database='RideShare', trusted_connection='yes')

        cursor = connection.cursor()

        sql = 'SELECT AddressId, Line1, Line2, ZipId, LocaleId FROM [Address]'

        addresses = []

        for row in cursor.execute(sql):
            addresses.append(address(line1=row[1], line2=row[2], addressid=row[0]))

        return addresses


    def get_makemodels(self) -> list:
        connection = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', server='.', database='RideShare', trusted_connection='yes')

        cursor = connection.cursor()

        sql = 'SELECT MakeModelId, Make, Model FROM MakeModel'

        makemodels = []

        for row in cursor.execute(sql):
            makemodels.append(makemodel(city=row[1], state=row[2], makemodelid=row[0]))

        return makemodels