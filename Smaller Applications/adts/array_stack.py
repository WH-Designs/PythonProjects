from adts.array import Array


class ArrayStack:
    """ Class ArrayStack - representing a fixed-size stack using a 1D Array
                Stipulations:
                1. Must use an Array object as the internal data structure from the Array assignment.
                2. Must adhere to the docstring requirements per method, including raising
                   raising appropriate exceptions where indicated.
                               3. Must achieve a minimum of 92% code coverage through unit testing.
    """
    def __init__(self, max_size: int = 0, instance=None) -> None:
        """ Constructor
            Usage:  stack = ArrayStack(10)
            @:param size the desired size of the stack
            @:param instance an optional ArrayStack instance to deep copy data from.
            @:return none
            @:raises TypeError if instance is provided and it is not an ArrayStack instance
        """
        self._stack = Array(max_size)

        self.max_size = max_size

        self._top = 0

        if instance is not None:
            if not isinstance(instance, ArrayStack):
                raise TypeError('Instance is not an ArrayStack instance')

            self._stack = Array(instance=instance._stack)

    @staticmethod
    def clone(instance):
        """ Clone the stack
                Usage:  stack = ArrayStack.clone(instance)
                @:param instance an ArrayStack instance to deep copy data from.
                @:return a deep object copy of the stack
                @:raises TypeError if instance is provided and it is not an ArrayStack instance
        """
        if instance is not None:
            if not isinstance(instance, ArrayStack):
                raise TypeError('Instance is not an ArrayStack instance')

        return ArrayStack(instance=instance)

    def push(self, item):
        """ Push an item onto the stack
                Usage:   stack.push(item)
                @:param item to enqueue
                @:return none
                @:raises IndexError if the stack is full
        """
        if self.full:
            raise IndexError('Array Stack is Full')
        else:
            self._stack[self._top] = item

            self._top += 1

    def pop(self):
        """ Pop an item from the stack and return the item
                Usage:   item = stack.pop()
                @:return item that is popped
                @:raises IndexError if the stack is empty
        """
        if self.empty:
            raise IndexError('Array Stack is empty')
        else:
            self._top -= 1

            item = self._stack[self._top]

            self._stack.resize(self._top)

            return item

    def clear(self) -> None:
        """ Clear the stack
                Usage: stack.clear():
                @:return none
        """
        self._stack.resize(0)

        self._top = 0

    @property
    def top(self):
        """ Get the item at the top of the stack
                Usage:   item = stack.top
                @:return item that is at the top of the stack
                @:raises IndexError if the stack is empty
        """
        if self.empty:
            raise IndexError('Array Stack is empty')

        item = self._stack[self._top - 1]

        return item

    @property
    def size(self) -> int:
        """ Get the size of the number of items on the stack
                Usage:   size = stack.size
                @:return size the number of items on the stack
        """
        return len(self._stack)

    @property
    def full(self) -> bool:
        """ Check whether the stack is full
                Usage:   full = stack.full
                @:return full boolean as to whether the stack is full
        """
        return self._top == self.max_size

    @property
    def empty(self) -> bool:
        """ Check whether the stack is empty
                Usage:   empty = stack.empty
                @:return empty boolean as to whether the stack is empty
        """
        return self._top == 0

    def __eq__(self, other) -> bool:
        """ Equality operator ==
            Usage: stack1 == stack2
            @:param other the instance to compare self to
            @:return true if the stacks are equal (deep check)
        """
        if not isinstance(other, ArrayStack):
            return False

        if len(self._stack) != len(other._stack):
            return False

        return self._stack == other._stack

    def __len__(self) -> int:
        """ len operator for getting length of the stack (size of array)
            Usage: length = len(stack)
            @:return the length of the Stack (size of array)
        """
        return len(self._stack)

    def __str__(self) -> str:
        """ Return a string representation of the data and structure
                Usage: print(stack):
                @:return str the string representation of the data and structure
        """
        return f'Top index: {self._top} {str(self._stack)}'
