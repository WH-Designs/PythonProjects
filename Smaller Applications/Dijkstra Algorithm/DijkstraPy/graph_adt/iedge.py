from abc import ABC, abstractmethod
from typing import Any


class IEdge(ABC):

    @property
    @abstractmethod
    def weight(self) -> float:
        pass

    @property
    @abstractmethod
    def data(self) -> Any:
        pass

    @property
    @abstractmethod
    def destination(self) -> 'IVertex':
        pass
