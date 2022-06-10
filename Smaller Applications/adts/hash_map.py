from typing import Any

from adts.array import Array
from adts.linked_list import LinkedList
from adts.list_node import ListNode
from adts.pair import Pair


class HashMap:
    """ Class HashMap - representing a HashMap (dictionary) where the
        buckets are based on an Array and the chains are based on LinkedLists
            Stipulations:
            1. Must use an Array<LinkedList<Pair>> as the internal data structure from the
               Array, LinkedList and Pair assignments.
            2. Must adhere to the docstring requirements per method, including raising
               raising appropriate exceptions where indicated.
            3. Must achieve a minimum of 92% code coverage through unit testing.
    """

    def __init__(self, max_size: int, hash_function) -> None:
        """ Constructor
            Usage:  hash_map = hash_map(23, hash_function)
            @:param max_size the desired max size of the HashMap
            @:param hash_function the desired hash function
            @:return none
        """
        self._hash_map = Array(max_size)
        self._hash_function = hash_function
        self._count = 0  # number of items stored in Hash Map

        for i in range(max_size):
            self._hash_map[i] = LinkedList()

    @staticmethod
    def clone(instance):
        """ Clone the hash map
            Usage:  hash_map = HashMap.clone(instance)
            @:param instance an HashMap instance to deep copy data from.
            @:return a deep object copy of the hash map
            @:raises TypeError if instance is provided and it is not an HashMap instance
        """
        if instance is not None:
            if not isinstance(instance, HashMap):
                raise TypeError('Instance is not an HashMap instance')

        new_instance = instance

        return new_instance

    def __getitem__(self, key):
        """ Bracket operator for getting an item value
            Usage: item = array[key]
            @:param key the key of the desired value
            @:return the item value associated with the key
            @:raises KeyError if the key is not present in the hashmap
        """
        bucket_index = self._hash_function(key)

        for item_pair in self._hash_map[bucket_index]:
            if item_pair[0] == key:
                return item_pair[1]

        raise KeyError('Key is not found')

    def __setitem__(self, key: Any, value: Any) -> None:
        """ Bracket operator for inserting a key/value pair into the hash map
            Usage: hash_map[key] = val
            @:param key the desired key set
            @:param value the value associated with the key
            @:return none
        """
        key_value_pair = Pair(key, value)
        bucket_index: int = self._hash_function(key)

        node: ListNode = (self._hash_map[bucket_index]).head
        while node is not None:
            if node.item[0] == key:
                node.item = Pair(key, value)
                return
            node = node.next
        self._hash_map[bucket_index].append(key_value_pair)
        self._count += 1

    def __len__(self) -> int:
        """ len operator for getting size of the hash map (number of key/value pairs)
            Usage: length = len(hash_map)
            @:return the size of the hash map
        """
        return self._count

    def resize(self, new_table_size: int, new_hash_function) -> None:
        """ Rehash a hash map
            Usage: hash_map.rehash(new_table_size, new_hash_function)
            @:param new_table_size the desired new table size
            @:param new_hash_function the desired new hash function
            @:return none
        """
        new_hash_map = HashMap(new_table_size, new_hash_function)

        for key, value in self:
            new_hash_map[key] = value

        self = new_hash_map

    def __eq__(self, other) -> bool:
        """ Equality operator ==
            Usage: array1 == array2
            @:param other the instance to compare self to
            @:return true if the arrays are equal (deep check)
        """
        if type(other) != type(self):
            return False

        return True

    def __iter__(self):
        """ Iterator operator
            Usage: for key, value in hash_map:
            @:return yields the key at the index
            @:return yields the value at the index
        """
        for bucket in self._hash_map:
            for pair in bucket:
                yield pair[0], pair[1]

    def __delitem__(self, key) -> None:
        """ Delete an item in the hash map. Does not resize the buckets, but does remove the associated chain link.
            Usage: del hash_map[key]
            @:param key the desired key to delete
            @:return none
            @:raises KeyError if the key is not found
        """
        if key in self:
            bucket_index = self._hash_function(key)

            del self._hash_map[bucket_index]

            self._count -= 1
        else:
            raise KeyError('Key not found')

    def __contains__(self, key) -> bool:
        """ Contains operator (in)
            Usage: if 3 in hash_map:
            @:param key the desired key to check whether it's in the hash_map
            @:return true if the hash_map contains the key
        """
        bucket_number = self._hash_function(key)

        for pair in self._hash_map[bucket_number]:
            if pair[0] == key:
                return True

        return False

    def clear(self) -> None:
        """ Clear the hash map
            Usage: hash_map.clear():
            @:return none
        """
        self._hash_map.clear()

        for i in range(len(self._hash_map)):
            self._hash_map[i] = LinkedList()

        self._count = 0

    def __str__(self) -> str:
        """ Return a string representation of the data and structure
            Usage: print(hash_map):
            @:return str the string representation of the data and structure
        """
        return str(self._hash_map)

    def keys(self):
        """ Returns a view object. The view object contains the keys of the dictionary, as a list.
            Usage: keys = hash_map.keys()
            @:return list a list containing the keys of the dictionary
        """
        keys = list()

        for bucket in self._hash_map:
            for pair in bucket:
                keys.append(pair[0])

        return keys

    def values(self):
        """ Returns a view object. The view object contains the values of the dictionary, as a list.
            Usage: values = hash_map.values()
            @:return list a list containing the values of the dictionary
        """
        values = list()

        for bucket in self._hash_map:
            for pair in bucket:
                values.append(pair[1])

        return values

    def items(self):
        """ Returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.
            Usage: items = hash_map.items()
            @:return items as a tuples in a list of the key/value pairs of the dictionary
        """
        items = list()

        for key, value in self:
            items.append((key, value))

        return items
