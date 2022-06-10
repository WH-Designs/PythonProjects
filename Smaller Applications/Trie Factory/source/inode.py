from abc import ABC, abstractmethod


class INode:

    @property
    @abstractmethod
    def key(self) -> str:
        pass

    @property
    @abstractmethod
    def is_terminal(self) -> bool:
        pass

    @is_terminal.setter
    @abstractmethod
    def is_terminal(self, state: bool) -> None:
        pass

    @property
    @abstractmethod
    def parent(self) -> "INode":
        pass

    @parent.setter
    @abstractmethod
    def parent(self, new_parent: "INode") -> None:
        pass

    @property
    @abstractmethod
    def children(self) -> dict:
        pass

    @property
    @abstractmethod
    def word(self) -> str:
        pass

    @abstractmethod
    def get_by_prefix(self) -> list:
        pass

    @abstractmethod
    def get_terminal_children(self) -> list:
        pass

    @abstractmethod
    def remove(self) -> None:
        pass

    @abstractmethod
    def clear(self) -> None:
        pass
