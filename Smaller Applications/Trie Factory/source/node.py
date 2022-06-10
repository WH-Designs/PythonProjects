from inode import INode


class Node(INode):
    def __init__(self, key: str = '', parent: INode = None, is_terminal: bool = False):
        self._key: str = key
        self._is_terminal: bool = is_terminal
        self._parent: INode = parent
        self._children: dict = dict()

    @property
    def key(self) -> str:
        return self._key

    @property
    def is_terminal(self) -> bool:
        return self._is_terminal

    @is_terminal.setter
    def is_terminal(self, terminal: bool) -> None:
        self._is_terminal = terminal

    @property
    def parent(self) -> "INode":
        return self._parent

    @property
    def children(self) -> dict:
        return self._children

    @property
    def word(self) -> str:
        if not self._is_terminal:
            return ''

        the_word_stack = []  # stack
        current = self

        while current._parent is not None:
            the_word_stack.append(current.key)
            current = current.parent

        return_word = ''
        for ch in reversed(the_word_stack):
            return_word += ch

        return return_word

    def get_by_prefix(self) -> list:
        if self._is_terminal:
            yield self.word

        for node in self.children.values():
            for item in node.get_by_prefix():
                yield item

    def get_terminal_children(self) -> list:
        for key, node in self._children:
            if node.is_terminal:
                yield node

            for grand_key, grand_child in node._children:
                if grand_child.is_terminal:
                    yield grand_child

    def remove(self) -> None:
        self._is_terminal = False
        del self.parent.children[self._key]

    def clear(self) -> None:
        for key, node in self._children:
            self._children[node] = None
