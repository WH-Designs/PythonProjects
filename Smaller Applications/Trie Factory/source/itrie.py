from abc import abstractmethod


class ITrie:

    @property
    @abstractmethod
    def count(self) -> int:
        pass

    @property
    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def add(self, word: str) -> None:
        pass

    @abstractmethod
    def remove(self, word: str) -> None:
        pass

    @abstractmethod
    def contains_word(self, word: str) -> bool:
        pass

    @abstractmethod
    def contains_prefix(self, prefix: str) -> bool:
        pass

    @abstractmethod
    def search_by_prefix(self, prefix: str) -> list:
        pass

    @abstractmethod
    def clear(self) -> None:
        pass

    @abstractmethod
    def __iter__(self) -> object:
        pass
