from adts.array import Array


class Array2D:
    """ Class Array2D - representing 2D data using a 1D array
        Stipulations:
            1. Must use an Array object as the internal data structure from the Array assignment.
            2. Must adhere to the docstring requirements per method, including raising
               raising appropriate exceptions where indicated.
            3. Must achieve a minimum of 92% code coverage through unit testing.
    """

    class _Row:
        """ Private inner class _Row - represents a row in the 2D array
        """

        def __init__(self, array2d: 'Array2D', row_index: int) -> None:
            """ Constructor - represents a row in the 2D array
                Usage:  row = _Row(array2d, row_index)
                @:param array2d the corresponding Array2D that the row belongs to.
                @:param row_index the row index of the row in question
                @:return none
            """
            self._array2d = array2d
            self._row_index = row_index

        def __getitem__(self, column_index: int):
            """ Bracket operator for getting an item
                Usage: val = array2d[row_index][column_index]
                @:param column_index the desired column_index
                @:return the item at array2d[row_index][column_index]
                @:raises IndexError if the location is out of bounds
            """
            return self._array2d.getitem(self._row_index, column_index)

        def __setitem__(self, column_index, data: int):
            """ Bracket operator for setting an item
                        Usage: array2d[row_index][column_index] = val
                        @:param column_index the desired column_index
                        @:return the item at array2d[row_index][column_index]
                        @:raises IndexError if the location is out of bounds
            """
            self._array2d.setitem(self._row_index, column_index, data)

    def __init__(self, row_len: int = 0, column_len: int = 0, instance=None) -> None:
        """ Constructor
            Usage:  array = Array(10)
            @:param size the desired size of the Array
            @:param instance an optional Array2D instance to deep copy data from.
            @:return none
            @:raises TypeError if instance is provided and it is not a LinkedList instance
        """
        self._items2d = Array(row_len * column_len)
        self._row_len = row_len
        self._column_len = column_len
        if instance is not None:
            if not isinstance(instance, Array2D):
                raise TypeError('Instance is not Array2D instance')
            else:
                self._items2d = instance._items2d
                self._column_len = instance._column_len
                self._row_len = instance._row_len

    @staticmethod
    def clone(instance):
        """ Clone the array2d
            Usage:  array2d = Array2D.clone(instance)
            @:param instance an Array instance to deep copy data from.
            @:return a deep object copy of the array2d
            @:raises TypeError if instance is provided and it is not an Array2D instance
        """
        if instance is not None:
            if not isinstance(instance, Array2D):
                raise TypeError('Instance is not an Array2D instance')

        return Array2D(instance=instance)

    def __getitem__(self, row_index: int):
        """ Bracket operator for getting an item
            Usage: val = array2d[row_index][column_index]
            @:param row_index the desired index
            @:return the _Row at the row_index
            @:raises IndexError if the index is out of bounds
        """
        # TODO: do bounds checking
        self.index_helper(row_index, 'r')

        return self._Row(self, row_index)

    def getitem(self, row_index: int, column_index: int):
        """ Helper method for getting an item
            Usage: val = array2d.getitem(row_index, column_index)
            @:param row_index the desired row_index
            @:param column_index the desired column_index
            @:return the item at the row_index, column_index
            @:raises IndexError if the index is out of bounds
        """
        # TODO: Bounds checking to raise exceptions
        self.index_helper(row_index, 'r')
        self.index_helper(column_index, 'c')

        actual_index_in_1D = row_index * self._column_len + column_index  # TODO: figure out mapping formula from 2D (row, col) --> 10 (index)

        return self._items2d[actual_index_in_1D]

    def setitem(self, row_index: int, column_index: int, data) -> None:
        """ Helper method for setting an item
            Usage: array2d[row_index][column_index] = val
            @:param row_index the desired row_index to set
            @:param column_index the desired column_index to set
            @:param data the desired data to set at indexes
            @:raises IndexError if the index is out of bounds
            @:return none
        """
        # TODO: Bounds checking to raise exceptions
        self.index_helper(row_index, 'r')
        self.index_helper(column_index, 'c')

        actual_index = row_index * self._column_len + column_index  # TODO: figure out mapping formula from 2D (row, col) --> 10 (index)

        self._items2d[actual_index] = data

    @property
    def columns_len(self):
        """ len method for the length of the columns
                Usage: column_length = array2d.columns_len
                @:return the length of the columns
        """
        return self._column_len

    @property
    def rows_len(self) -> int:
        """ len method for the length of the rows
            Usage: row_length = array2d.rows_len
            @:return the length of the rows
        """
        return self._row_len

    def resize_columns(self, new_columns_len: int) -> None:
        """ Resize the length of the columns
            Usage: array2d.resize_columns(new_columns_len)
            @:param new_columns_len the desired new length of the columns
            @:raises ValueError if the new_columns_len does not make sense
            @:return none
        """
        # new_items = Array(self._row_len * new_columns_len)
        # smaller_col_len = self._column_len if self._column_len < new_columns_len else new_columns_len
        #
        # for row in range(self._row_len):
        #     new_row_offset = row * new_columns_len
        #     old_row_offset = row * self._column_len
        #     for col in range(smaller_col_len):
        #         new_items[new_row_offset + col] = self._items2d[old_row_offset + col]
        #
        # self._items2d = new_items
        # self._column_len = new_columns_len

        if new_columns_len > self._column_len:
            new_lis = []
            a = 0
            for i in range(len(self._items2d)):
                new_lis.append(self._items2d[i])
                a += 1
                if a == self._column_len:
                    new_lis.append(None)
                    a = 0
            # self._items2d = new_lis
        else:
            new_list = []
            a = 0
            for i in range(len(self._items2d)):
                if a == new_columns_len:
                    a = 0
                else:
                    new_list.append(self._items2d[i])
                    a += 1
                    # print(new_list)
            # self._column_len = new_columns_len

    def resize_rows(self, new_rows_len: int) -> None:
        """ Resize the length of the rows
                Usage: array2d.resize_rows(new_row_len)
                @:param new_rows_len the desired new length of the rows
                @:raises ValueError if the new_rows_len does not make sense
                @:return none
        """
        if new_rows_len > self._row_len:
            resized_array = [None] * new_rows_len
            for i in range(len(self._items2d)):
                resized_array.insert(i, self._items2d[i])
            self._row_len = new_rows_len
            # self._items2d = resized_array
        else:
            new_list = []
            self._row_len = new_rows_len
            for i in range(self._row_len):
                new_list.append(self._items2d[i])

    def __eq__(self, other) -> bool:
        """ Equality operator ==
            Usage: array1 == array2
            @:param other the instance to compare self to
            @:return true if the arrays are equal (deep check)
        """
        if not isinstance(other, Array2D):
            return False

        return self._items2d == other._items2d

    def __contains__(self, item) -> bool:
        """ Contains operator (in)
            Usage: if 3 in array2d:
            @:param item the desired item to check whether it's in the array
            @:return true if the array contains the item
            @:raises TypeError if other is not the right type to compare
        """
        for i in range(len(self._items2d)):
            if item == self._items2d[i]:
                return True

        return False

    def clear(self) -> None:
        """ Clear the array2d
                Usage: array2d.clear():
                @:return none
        """
        self._items2d = [None] * len(self._items2d)

    def __str__(self) -> str:
        """ Return a string representation of the data and structure
                Usage: print(array2d):
                @:return str the string representation of the data and structure
        """
        return str(self._items2d)

    def index_helper(self, _index, _str):
        if _str == 'r':
            if _index < 0 or _index >= self._row_len:
                raise IndexError(f'{_index} is out of bounds for an Array2D with row size: {self.rows_len}')
        elif _str == 'c':
            if _index < 0 or _index >= self._column_len:
                raise IndexError(f'{_index} is out of bounds for an Array2D with row size: {self.columns_len}')
