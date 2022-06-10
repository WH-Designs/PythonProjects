from abc import ABC, abstractmethod
from typing import Any


class IVertex(ABC):

    @property
    @abstractmethod
    def data(self) -> Any:
        pass

    @property
    @abstractmethod
    def edges(self) -> list:
        pass

    @property
    @abstractmethod
    def processed(self) -> bool:
        pass

    @abstractmethod
    def add_edge(self, data: Any, destination_vertex: 'IVertex', weight: float) -> None:
        pass

    @abstractmethod
    def remove_edge(self, data: Any, destination_vertex: 'IVertex') -> None:
        pass

    @abstractmethod
    def remove_edge(self, destination_vertex: 'IVertex') -> None:
        pass
