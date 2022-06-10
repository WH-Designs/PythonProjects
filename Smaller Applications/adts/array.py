
class Array:
    """ Class Array - representing 1D data using a Python List
        Stipulations:
            1. Must use a sized Python list as the internal data structure
            2. Must adhere to the docstring requirements per method, including raising
               raising appropriate exceptions where indicated.
           3. Must achieve a minimum of 92% code coverage through unit testing.
    """

    def __init__(self, size: int = 0, instance=None) -> None:
        """ Constructor
            Usage:  array = Array(10)
            @:param size the desired size of the Array (optional if providing instance)
            @:param instance an optional Array instance to deep copy data from.
            @:return none
            @:raises TypeError if instance is provided and it is not an Array instance
        """
        if instance is not None:
            if not isinstance(instance, Array):
                raise TypeError('Instance is not an Array instance')
            self._items = [None] * len(instance._items)
            for i in range(len(instance)):
                self._items[i] = instance[i]
        else:
            self._items = [None] * size

    @staticmethod
    def clone(instance):
        """ Clone the array
            Usage:  array = Array.clone(instance)
            @:param instance an Array instance to deep copy data from.
            @:return a deep object copy of the array
            @:raises TypeError if instance is provided and it is not an Array instance
            """
        if instance is not None:
            if not isinstance(instance, Array):
                raise TypeError('Instance is not an Array instance')
        #     array1 = [None] * len(instance._items)
        #     for i in range(len(instance)):
        #         array1[i] = instance[i]
        #
        # return instance
        return Array(instance=instance)

    @staticmethod
    def to_array(lst: list):
        array = Array(len(lst))

        for i in range(len(lst)):
            array[i] = lst[i]

        return array

    def __getitem__(self, index: int):
        """ Bracket operator for getting an item
            Usage: val = array[0]
            @:param index the desired index
            @:return the item at the index
            @:raises IndexError if the index is out of bounds
        """
        return self._items[index]

    def __setitem__(self, index: int, data) -> None:
        """ Bracket operator for setting an item
            Usage: array[index] = val
            @:param index the desired index to set
            @:param data the desired data to set at index
            @:raises IndexError if the index is out of bounds
            @:return none
        """
        self._items[index] = data

    def __len__(self) -> int:
        """ len operator for getting length of the array
            Usage: for i in range(len(array))
            @:return the length of the Array
        """
        return len(self._items)

    def resize(self, new_size: int) -> None:
        """ Resize an Array
            Usage: array.resize(5)
            @:param new_size the desired new size
            @:return none
        """
        new_items = [None] * new_size

        smaller_size = len(self._items) if len(self._items) <= new_size else new_size

        for i in range(smaller_size):
            new_items[i] = self._items[i]

        self._items = new_items

    def __eq__(self, other) -> bool:
        """ Equality operator ==
            Usage: array1 == array2
            @:param other the instance to compare self to
            @:return true if the arrays are equal (deep check)
        """
        if not isinstance(other, Array):
            return False

        return self._items == other._items

    def __iter__(self):
        """ Iterator operator
            Usage: for item in array:
            @:return yields the item at index
        """
        for i in range(len(self._items)):
            yield self._items[i]

    def __delitem__(self, index: int) -> None:
        """ Delete an item in the array. Copies the array contents from index + 1 down
            to fill the gap caused by deleting the item and shrinks the array size down by one
            Usage: del array[0]
            @:param index the desired index to delete
            @:return none
        """
        del self._items[index]

    def __contains__(self, item) -> bool:
        """ Contains operator (in)
            Usage: if 3 in array:
            @:param item the desired item to check whether it's in the array
            @:return true if the array contains the item
        """
        for i in range(len(self._items)):
            if item == self._items[i]:
                return True

        return False

    def clear(self) -> None:
        """ Clear the array
            Usage: array.clear():
            @:return none
        """
        for i in range(len(self._items)):  # O(n)
            self._items[i] = None

        #self._items = [None] * len(self._items)   # O(1)

    def __str__(self) -> str:
        """ Return a string representation of the data and structure
            Usage: print(array):
            @:return str the string representation of the data and structure
        """
        return str(self._items)

    def merge(self, other) -> None:
        """Merges self's items with other's items, in a single order fashion.
        Usage: array.merge(other_array)
        @:param other: the second Array instance to merge with array
        @:return: none
        @:raises: TypeError if other is not an Array instance
        """
        if other is not None:
            if not isinstance(other, Array):
                raise TypeError('Instance is not an Array instance')

        # list1 = self._items
        # list2 = other
        # combined_list = list()
        #
        # a1 = len(list1)
        # b2 = len(list2)
        #
        # for i in range(max(a1, b2)):
        #     if i < a1:
        #         combined_list.append(list1[i])
        # if i < b2:
        #     combined_list.append(list2[i])
        #
        # self._items = combined_list

        # items = self._items
        items = self._items
        other_items = other

        len_of_items = len(items)
        len_of_other = len(other_items)

        new_list = list()

        for l in range(max(len_of_items, len_of_other)):
            if l < len_of_items:
                new_list.append(items[l])
            if l < len_of_other:
                new_list.append(other_items[l])

        self._items = new_list

        # newlist = []
        #
        # if len(self._items) >= len(other):
        #     for i in range(len(self._items)):
        #         if counter == 0:
        #             newlist[i] = self._items[i]
        #             counter = 1
        #         elif counter == 1:
        #             newlist[i] = other[i]
        #             counter = 0