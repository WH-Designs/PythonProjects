from abc import ABC, abstractmethod
from zip import zip
from locale import locale
from address import address
from vehicle import vehicle
from ride import ride
from user import user
from usertype import usertype
from makemodel import makemodel

class datarepository(ABC):
    @abstractmethod
    def add_user(self, user: user) -> None:
        pass

    @abstractmethod
    def get_user(self, username: str) -> user:
        pass

    @abstractmethod
    def delete_user(self, username: str) -> None:
        pass

    @abstractmethod
    def get_users(self) -> list:
        pass

    @abstractmethod
    def add_ride(self, ride: ride) -> None:
        pass

    @abstractmethod
    def get_ride(self, user: user) -> ride:
        pass

    @abstractmethod
    def get_rides(self) -> list:
        pass

    @abstractmethod
    def delete_ride(self, rideid: int) -> None:
        pass

    @abstractmethod
    def add_vehicle(self, vehicle: vehicle) -> None:
        pass

    @abstractmethod
    def delete_vehicle(self, vehicleid: int) -> None:
        pass

    @abstractmethod
    def get_vehicle(self, vehicleid: int) -> vehicle:
        pass

    @abstractmethod
    def get_address(self, addressid: int) -> address:
        pass

    @abstractmethod
    def add_address(self, address: address) -> None:
        pass

    @abstractmethod
    def get_zip(self, zipid: int) -> zip:
        pass

    @abstractmethod
    def add_zip(self, zip: zip) -> None:
        pass

    @abstractmethod
    def get_locale(self, localeid: int) -> locale:
        pass

    @abstractmethod
    def add_locale(self, locale: locale) -> None:
        pass

    @abstractmethod
    def get_usertype(self, usertypeid: int) -> usertype:
        pass

    @abstractmethod
    def get_usertypes(self) -> list:
        pass

    @abstractmethod
    def get_makemodel(self) -> makemodel:
        pass

    @abstractmethod
    def add_makemodel(self) -> None:
        pass

    @abstractmethod
    def get_zips(self) -> list:
        pass

    @abstractmethod
    def get_locales(self) -> list:
        pass

    @abstractmethod
    def get_addresses(self) -> list:
        pass

    @abstractmethod
    def get_makemodels(self) -> list:
        pass