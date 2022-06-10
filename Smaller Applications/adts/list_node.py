
class ListNode:
    """ ListNode - represents a node in a linked list
            Stipulations:
            1. Must adhere to the docstring requirements per method, including raising
               raising appropriate exceptions where indicated.
            2. Must achieve a minimum of 92% code coverage through unit testing.
    """

    def __init__(self, item, previous_node=None, next_node=None) -> None:
        """ Constructor - represents a row in the 2D array
            Usage:  node = _Node() or node = _Node(None, None) or node = _Node(previous_node, next_node)
            @:param item the item (data) to store in the node
            @:param previous_node the corresponding previous node of this node in the linked list
            @:param next_node the corresponding next node of this node in the linked list
            @:return none
        """
        self._item = item
        self._previous_node = previous_node
        self._next_node = next_node

    @property
    def item(self):
        """ Property for the item
            Usage: item = node.item
            @:return the item stored in the node
        """
        return self._item

    @item.setter
    def item(self, item) -> None:
        """ Setter for the item
            Usage: node.item = item
            @:param item the item to store in the node
            @:return none
        """
        self._item = item

    @property
    def previous(self):
        """ Property for the previous node
            Usage: previous_node = node.previous
            @:return the previous node of the node
        """
        return self._previous_node

    @previous.setter
    def previous(self, previous_node) -> None:
        """ Setter for the previous node
            Usage: node.previous = previous_node
            @:param previous_node the node's previous_node instance
            @:return none
        """
        self._previous_node = previous_node

    @property
    def next(self):
        """ Property for the next node
            Usage: next_node = node.next
            @:return the next node of the node
        """
        return self._next_node

    @next.setter
    def next(self, next_node) -> None:
        """ Setter for the next node
            Usage: node.next = next_node
            @:param next_node the node's next_node instance
            @:return none
        """
        self._next_node = next_node

    def __eq__(self, other) -> bool:
        """ Equality operator ==
            Usage: array1 == array2
            @:param other the instance to compare self to
            @:return true if the arrays are equal (deep check)
        """
        if not isinstance(other, ListNode):
            return False

        return self._item is other._item and self._previous_node is other._previous_node and self._next_node is other._next_node

    # def __iter__(self):
    #     """ Iterator operator
    #         Usage: for item in LinkedList:
    #         @:return yields the item at ListNode
    #     """
    #     raise NotImplementedError
    #
    # def __len__(self) -> int:
    #     """ len operator for getting length of the linked list
    #         Usage: size = len(linked_list)
    #         @:return the length of the LinkedList
    #     """
    #     raise NotImplementedError

    def __str__(self) -> str:
        """ Return a string representation of the data and structure
            Usage: print(node):
            @:return str the string representation of the data and structure
        """
        return f'ListNode with Item: {self._item}, Previous Node: {self._previous_node}, Next Node: {self._next_node}'
