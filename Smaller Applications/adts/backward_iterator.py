from adts.list_iterator import ListIterator
from adts.list_node import ListNode


class BackwardIterator(ListIterator):
    """ Class BackwardIterator - concrete child class of ListIterator.
            Stipulations:
            1. Must adhere to the docstring requirements per method, including raising
                raising appropriate exceptions where indicated.
            2. Must achieve a minimum of 92% code coverage through unit testing.
    """

    def __init__(self, node: ListNode) -> None:
        """ Constructor for the ForwardIterator base class
            Usage:  iterator = ForwardIterator(list_node).
            @:param node the node that the iterator will point to
            @:return none
            @:raises TypeError if the node provided is None or it is not a ListNode instance
        """
        raise NotImplementedError

    def move_next(self) -> None:
        """ Move the iterator forward.
            Usage: iterator.move_next()
            @:return none
        """
        raise NotImplementedError

    def reset(self) -> None:
        """ Reset the iterator the beginning.
            Usage: iterator.reset()
            @:return none
        """
        raise NotImplementedError

    def __iter__(self):
        """ Iterator operator
            Usage: for item in array:
            @:return yields the item at index
        """
        raise NotImplementedError

    def __eq__(self, other) -> bool:
        """ Equality method - should return true if the instances are both pointing to the same node and are done
            Usage: iter1 == iter2
            @:param other the instance to compare to
        """
        raise NotImplementedError

    def __str__(self) -> str:
        """Str method to return a string representation of the data and structure
            Usage: print(iterator):
            @:return str the string representation of the data and structure
        """
        raise NotImplementedError
