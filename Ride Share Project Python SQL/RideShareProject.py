import pyodbc
from sql_server_repo import SqlServerRepository
from zip import zip
from locale import locale
from address import address
from vehicle import vehicle
from ride import ride
from user import user
from usertype import usertype
from makemodel import makemodel

def main():

    count = 1

    repo = SqlServerRepository()

    print("Welcome to ride share!\n")

    returning = input('Are you a returning user? Y/N\n')

    if returning == 'N':

        driver_or_rider = input('Are you driver or rider?\n')

        #Register as a rider
        if driver_or_rider == 'rider':

            #Rider info
            new_username = input('Enter a new username: \n')
            new_password = input('Enter a new password: \n')
            new_address_line1 = input('Enter your home address line 1: \n')
            new_city = input('Enter your city: \n')
            new_state = input('enter your state: \n')
            new_zip = input('enter you zip code: \n')
            new_phone = input('Enter your phone number: \n')
            new_email = input('Enter your email address: \n')

            #Add all the info to sql
            zip1=zip(new_zip)
            locale1=locale(new_city, new_state)
            repo.add_zip(zip1)
            repo.add_locale(locale1)

            zips = repo.get_zips()

            for i in zips:
                if i.code == zip1.code:
                    zip1.zipid = i.zipid

            locales = repo.get_locales()

            for i in locales:
                if (i.city == locale1.city) and (i.state == locale1.state):
                    locale1.localeid = i.localeid

            address1=address(new_address_line1, '', zip1.zipid, locale1.localeid)
            repo.add_address(address1)

            addresses = repo.get_addresses()

            for i in addresses:
                if i.line1 == address1.line1:
                    address1.addressid = i.addressid

            repo.add_user(user(new_username, new_password, address1.addressid, new_phone, new_email, 0.0, 1))

            print('Rider has been created!')

        #Register as a driver
        elif driver_or_rider == 'driver':

            #Driver info
            new_username = input('Enter a new username: \n')
            new_password = input('Enter a new password: \n')
            new_address_line1 = input('Enter your home address line 1: \n')
            new_city = input('Enter your city: \n')
            new_state = input('enter your state: \n')
            new_zip = input('enter you zip code: \n')
            new_phone = input('Enter your phone number: \n')
            new_email = input('Enter your email address: \n')
            new_vehicle_licenseplate = input('Enter your vehicles licenseplate: \n')
            new_vehicle_make = input('Enter your vehicles make: \n')
            new_vehicle_model = input('Enter you vehicles model: \n')

            #Add all the info to sql
            zip1=zip(new_zip)
            locale1=locale(new_city, new_state)
            repo.add_zip(zip1)
            repo.add_locale(locale1)

            zips = repo.get_zips()

            for i in zips:
                if i.code == zip1.code:
                    zip1.zipid = i.zipid

            locales = repo.get_locales()

            for i in locales:
                if (i.city == locale1.city) and (i.state == locale1.state):
                    locale1.localeid = i.localeid

            address1=address(new_address_line1, '', zip1.zipid, locale1.localeid)
            repo.add_address(address1)

            addresses = repo.get_addresses()

            for i in addresses:
                if i.line1 == address1.line1:
                    address1.addressid = i.addressid

            repo.add_user(user(new_username, new_password, address1.addressid, new_phone, new_email, 0.0, 2))

            makemodel1=makemodel(new_vehicle_make, new_vehicle_model)

            repo.add_makemodel(makemodel1)

            makemodels = repo.get_makemodels()

            for i in makemodels:
                if (i.make == makemodel1.make) and (i.model == makemodel1.model):
                    makemodel1.makemodelid = i.makemodelid

            vehicle1=vehicle(new_vehicle_licenseplate, makemodel1.makemodelid)

            print('Driver has been created!')

            
    else:
        #Login as a returning user
        print('Login Page\n')

        username = input('Enter your username: \n')
        password = input('Enter you password: \n')

        user: user = repo.get_user(username)

        if password != user.password:
            print('Access Denied')
        else:    
            if user.usertypeid == 1:
                #Create a ride request
                ride_request = input('would you like to request a ride? Y/N\n')

                if ride_request == 'Y':
                    #Provide Physcial Location
                    pickuplocation = input('Enter your current location: ')

                    #Provide desired pickup time
                    desiredpickuptime = input('Enter your desired pickuptime: ')

                    ride1=ride(user.userid, False, False, desiredpickuptime, pickuplocation)

                    repo.add_ride(ride1)

                else:
                    rides = repo.get_rides()

                    payment = input('Do you want to pay for your ride? Y/N\n')

                    for i in rides:
                        if i.riderid == user.userid:
                            if i.ridestatus == True:
                                if payment == 'Y':
                                    i.paymentstatus = True
                                else:
                                    continue

            elif user.usertypeid == 2:
                #Browse available rides
                rides = repo.get_rides()

                for i in rides:
                    if i.ridestatus == False:
                        print(f'Ride {count}: ' + i)
                        count += 1

                #Accept a ride
                ride_selected = input('Enter the number you want to accept: \n')

                ride_driving = rides[ride_selected - 1]

                #Provide ETA
                eta_given = input('Provide an ETA for the ride: \n')

                ride_driving.eta = eta_given

                #Send driver info to rider
                driver_info = []
                
                vehicle1 = repo.get_vehicle(ride_driving.vehicleid)

                makemodel1 = repo.get_makemodel(vehicle1.makemodelid)

                driver_info.append(user.username, makemodel1.make, makemodel1.model, vehicle1.licenseplate, eta_given)
                
                print('Here is the driver info:\n')

                for i in driver_info:
                    print(f'{i}\n')

                ride_driving.ridestatus = True

if __name__ == '__main__':
    main()