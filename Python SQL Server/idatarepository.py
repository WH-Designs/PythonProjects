
from abc import ABC, abstractmethod
from credential import Credential

class IDataRepository(ABC):
    @abstractmethod
    def add_credential(self, credential: Credential) -> None:
        pass

    @abstractmethod
    def get_credentials(self) -> list:
        pass
    
    @abstractmethod
    def get_credential(self, username: str) -> Credential:
        pass

    @abstractmethod
    def delete_credential(self, username: str) -> None:
        pass
