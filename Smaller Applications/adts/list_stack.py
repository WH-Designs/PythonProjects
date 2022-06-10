from adts.linked_list import LinkedList


class ListStack:
    """ Class ListStack - representing a stack using a LinkedList
            Stipulations:
            1. Must use a LinkedList as the internal data structure from the LinkedList assignment.
            2. Must adhere to the docstring requirements per method, including raising
               raising appropriate exceptions where indicated.
            3. Must achieve a minimum of 92% code coverage through unit testing.
    """

    def __init__(self, instance=None) -> None:
        """ Constructor
            Usage:  stack = ListStack()
            @:param instance an optional ListStack instance to deep copy data from.
            @:return none
            @:raises TypeError if instance is provided and it is not an ListStack instance
        """
        self._stack = LinkedList()
        self._top = 0

        if instance is not None:
            if not isinstance(instance, ListStack):
                raise TypeError('Instance is not an ListStack instance')

            self._stack = LinkedList(instance=instance._stack)

    @staticmethod
    def clone(instance):
        """ Clone the stack
            Usage:  stack = ListStack.clone(instance)
            @:param instance an ListStack instance to deep copy data from.
            @:return a deep object copy of the stack
            @:raises TypeError if instance is provided and it is not an Stack instance
        """
        if instance is not None:
            if not isinstance(instance, ListStack):
                raise TypeError('Instance is not an ListStack instance')

        return ListStack(instance=instance)

    def push(self, item):
        """ Push an item onto the stack
            Usage:   stack.push(item)
            @:param item to push
            @:return none
        """
        self._stack.append(item)

    def pop(self):
        """ Pop an item from the stack and return the item
            Usage:   item = stack.pop()
            @:return item that is popped
            @:raises IndexError if the stack is empty
        """
        if self._stack.empty:
            raise IndexError('ListStack is empty')

        item = self._stack.last
        self._stack.remove_last()

        return item

    def clear(self) -> None:
        """ Clear the stack
            Usage: stack.clear():
            @:return none
        """
        self._stack.clear()

    @property
    def top(self):
        """ Get the item at the top of the stack
            Usage:   item = stack.top
            @:return item that is at the top of the stack
            @:raises IndexError if the stack is empty
        """
        if self._stack.empty:
            raise IndexError('ListStack is empty')

        return self._stack.last

    @property
    def size(self) -> int:
        """ Get the size of the number of items on the stack
            Usage:   size = stack.size
            @:return size the number of items on the stack
        """
        return len(self._stack)

    @property
    def empty(self) -> bool:
        """ Check whether the stack is empty
            Usage:   empty = stack.empty
            @:return empty boolean as to whether the stack is empty
        """
        return len(self._stack) == 0

    def __eq__(self, other) -> bool:
        """ Equality operator ==
            Usage: array1 == array2
            @:param other the instance to compare self to
            @:return true if the arrays are equal (deep check)
        """
        if not isinstance(other, ListStack):
            return False

        if len(other) != len(self._stack):
            return False

        return self._stack == other._stack

    def __len__(self) -> int:
        """ len operator for getting length of the stack
            Usage: length = len(stack)
            @:return the length of the Stack (number of items on the stack)
        """
        return len(self._stack)

    def __str__(self) -> str:
        """ Return a string representation of the data and structure
            Usage: print(stack):
            @:return str the string representation of the data and structure
        """
        return f'Top index: {self._top} {str(self._stack)}'
