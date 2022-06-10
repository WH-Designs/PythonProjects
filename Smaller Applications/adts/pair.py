class Pair:
    """ Class Pair - representing a Pair as a Tuple
            Stipulations:
            1. Must use a Python tuple as the internal data structure.
            2. Must adhere to the docstring requirements per method, including raising
               raising appropriate exceptions where indicated.
            3. Must achieve a minimum of 92% code coverage through unit testing.
    """

    def __init__(self, first=None, second=None, instance=None) -> None:
        """ Constructor
            Usage:  pair = Pair('My', 'Pair')
            @:param first the desired first part of the Pair
            @:param second the desired second part of the Pair
            @:param instance an optional Pair instance to deep copy data from.
            @:return none
            @:raises TypeError if instance is provided and it is not a Pair instance
        """
        if instance is not None:
            if not isinstance(instance, Pair):
                raise TypeError('Instance is not a pair')
            self._pair = (instance[0], instance[1])
        else:
            self._pair = (first, second)

    @staticmethod
    def clone(instance):
        """ Clone the pair
            Usage:  pair = Pair.clone(instance)
            @:param instance an Pair instance to deep copy data from.
            @:return a deep object copy of the pair
            @:raises TypeError if instance is provided and it is not an Pair instance
            """
        if not isinstance(instance, Pair):
            raise TypeError('Instance is not a pair')

        return Pair(instance[0], instance[1])

    def __getitem__(self, index: int):
        """ Bracket operator for getting an item from the pair. Only [0] and [1] are permitted for index.
            Usage: val = pair[0]
            @:param index the desired index
            @:return the item at the index
            @:raises IndexError if the index is out of bounds
        """
        if index not in [0, 1]:
            raise IndexError('Out of bounds')

        return self._pair[index]

    def __eq__(self, other) -> bool:
        """ Equality operator ==
            Usage: pair1 == pair2
            @:param other the instance to compare self to
            @:return true if the pairs are equal (deep check)
        """
        if not isinstance(other, Pair):
            return False

        return self._pair[0] == other[0] and self._pair[1] == other[1]

    def __iter__(self):
        """ Iterator operator
            Usage: for item in pair:
            @:return yields the item at index
        """
        for i in range(len(self._pair)):
            yield self._pair[i]

    def __contains__(self, item) -> bool:
        """ Contains operator (in)
            Usage: if 3 in pair:
            @:param item the desired item to check whether it's in the pair
            @:return true if the pair contains the item
        """
        return item in self._pair

    def __str__(self) -> str:
        """ Return a string representation of the data and structure
            Usage: print(pair):
            @:return str the string representation of the data and structure
        """
        return str(self._pair)
