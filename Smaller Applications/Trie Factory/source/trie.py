from inode import INode
from node import Node
from itrie import ITrie


class Trie(ITrie):
    def __init__(self):
        self._root: INode = Node(key='')
        self._count: int = 0

    @property
    def count(self) -> int:
        return self._count

    @property
    def is_empty(self) -> bool:
        return self._count == 0

    def add(self, word: str) -> None:
        travel: INode = self._root

        for ch in word:
            if ch not in travel.children.keys():
                new_node = Node(key=ch, parent=travel)
                travel.children[ch] = new_node
            travel = travel.children[ch]

        if travel.is_terminal: raise Exception(f'{word} already exists!')

        self._count += 1
        travel.is_terminal = True

    def remove(self, word: str) -> None:
        travel: INode = self._root

        for ch in word:
            if not travel.children[ch]:
                raise Exception('Prefix not found')
            travel = travel.children[ch]

        self._count -= 1
        travel.remove()

    def contains_word(self, word: str) -> bool:
        travel: INode = self._root

        for ch in word:
            if not travel.children[ch]:
                raise KeyError(f'Trie does not contain the word: {word}')
            travel = travel.children[ch]

        return travel != None

    def contains_prefix(self, prefix: str) -> bool:
        travel: INode = self._root

        for ch in prefix:
            if not travel.children[ch]:
                raise KeyError(f'Trie does not contain the prefix: {prefix}')
            travel = travel.children[ch]

        return travel != None

    def search_by_prefix(self, prefix: str) -> list:
        travel: INode = self._root

        for ch in prefix:
            if ch not in travel.children:
                return None

            travel = travel.children[ch]

        return travel.get_by_prefix()

    def clear(self) -> None:
        self._count = 0
        self._root = None

    def __iter__(self) -> object:
        travel: INode = self._root

        while not travel.is_terminal:
            for key, child in travel.children.items():
                yield key
                travel = child.children[key]
