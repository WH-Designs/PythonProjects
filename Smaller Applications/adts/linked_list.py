from typing import Any

from adts.backward_iterator import BackwardIterator
from adts.forward_iterator import ForwardIterator
from adts.list_node import ListNode


class LinkedList:
    """ Class LinkedList - representing an unordered linked list
        Depends on ListNode class to store the items, previous, and next nodes.
            Stipulations:
            1. Must manage the linked list using only two ListNode objects (_head and _tail)
            2. Must adhere to the docstring requirements per method, including raising
               raising appropriate exceptions where indicated.
            3. Must achieve a minimum of 92% code coverage through unit testing.
    """

    def __init__(self, instance=None) -> None:
        """ Constructor for the LinkedList
            Usage:  linked_list = LinkedList()
            @:param instance an optional instance of a LinkedList to deep copy from
            @:return none
            @:raises TypeError if instance is provided and it is not a LinkedList instance
        """
        self._head: ListNode = None
        self._tail: ListNode = None
        self._count: int = 0

        if instance is not None:
            if not isinstance(instance, LinkedList):
                raise TypeError('Instance is not LinkedList instance')

            travel = instance.head
            while travel is not None:
                # add the data to self
                # advance travel to it's next node
                self.append(travel.item)
                travel = travel.next

    @staticmethod
    def clone(instance):
        """ Clone the LinkedList
            Usage:  new_linked_list = LinkedList.clone(instance)
            @:param instance a LinkedList instance to deep copy data from.
            @:return a deep object copy of the linked list
            @:raises TypeError if instance is provided and it is not an LinkedList instance
        """
        if instance is not None:
            if not isinstance(instance, LinkedList):
                raise TypeError('Instance is not LinkedList instance')

        return LinkedList(instance=instance)

    def append(self, item) -> None:
        """ Append an item to the end of the list
            Usage: linked_list.append(item)
            @:param item the desired item to append to the linked list
            @:return none
        """
        new_node = ListNode(item)

        if self.empty:
            self._head = self._tail = new_node

        else:
            self._tail.next = new_node
            new_node.previous = self._tail
            self._tail = new_node

        self._count += 1

    def prepend(self, item) -> None:
        """ Prepend an item to the end of the list
            Usage: linked_list.prepend(item)
            @:param item the desired item to prepend to the linked list
            @:return none
        """
        new_node = ListNode(item)

        if self.empty:
            self._head = self._tail = new_node

        else:
            self._head.previous = new_node
            new_node.next = self._head
            self._head = new_node

        self._count += 1

    def insert_before(self, before_item, new_item) -> None:
        """ Insert a new item before a specified item
            Usage: linked_list.insert_before(before_item, new_item)
            @:param before_item the item that the user wishes to insert before
            @:param new_item the desired item to insert
            @:return none
            @:raises KeyError if before_item is not found
        """
        travel = self._head

        while travel is not None and travel.item != before_item:
            travel = travel.next

        if travel is None:
            raise KeyError(f'{before_item} was not found')

        if travel == self._head:
            self.prepend(new_item)

            self._count += 1
        else:
            # middle case
            new_node = ListNode(new_item, travel.previous, travel)
            travel.previous.next = new_node
            travel.previous = new_node

            self._count += 1

    def insert_after(self, after_item, new_item) -> None:
        """ Insert a new item after a specified item
            Usage: linked_list.insert_after(after_item, new_item)
            @:param before_item the item that the user wishes to insert before
            @:param new_item the desired item to insert
            @:return none
            @:raises KeyError if before_item is not found
        """
        travel = self._tail

        while travel is not None and travel.item != after_item:
            travel = travel.previous

        if travel is None:
            raise KeyError(f'{after_item} was not found')

        if travel == self._tail:
            self.append(new_item)

            self._count += 1
        else:
            # middle case
            new_node = ListNode(new_item, travel.next, travel)
            travel.next.previous = new_node
            travel.next = new_node

            self._count += 1

    @property
    def head(self) -> ListNode:
        """ Return the ListNode instance pointing at the head of the linked list.
            Note: this method should be used for debug and test purposes only.
            Usage: head = linked_list.head
            @:return head the ListNode instance representing the head of the linked list
        """
        return self._head

    @property
    def tail(self) -> ListNode:
        """ Return the ListNode instance pointing at the tail of the linked list.
            Note: this method should be used for debug and test purposes only.
            Usage: tail = linked_list.tail
            @:return tail the ListNode instance representing the tail of the linked list
        """
        return self._tail

    @property
    def first(self) -> Any:
        """ Return the item at the head of the linked list.
            Usage: first_item = linked_list.first
            @:return first the item stored in the head of the list
            @:raises IndexError if the list is empty
        """
        # logic for raise
        if self.empty:
            raise IndexError('LinkedList is empty')

        return self._head.item

    @property
    def last(self) -> Any:
        """ Return the item at the tail of the linked list.
            Usage: last_item = linked_list.last
            @:return last the item stored in the tail of the list
            @:raises IndexError if the list is empty
        """
        # logic for raise
        if self.empty:
            raise IndexError('LinkedList is empty')

        return self._tail.item

    def clear(self) -> None:
        """ Clear the linked list
            Usage: linked_list.clear():
            @:return none
        """
        travel = self._head

        while travel is not None:
            travel.item = None
            travel = travel.next

        self._count = 0

    def extract(self, item):
        """ Extract an item from the Linked List
            @:param item the item to remove
            @:return: None
            @:raises: KeyError if the item is not found
        """
        travel = self._head

        while travel is not None and travel.item != item:
            travel = travel.next

        if travel is None:
            raise KeyError(f'{item} was not found')

        if travel is self._head:
            self.remove_first()
        elif travel is self._tail:
            self.remove_last()
        else:
            travel.previous.next = travel.next
            travel.next.previous = travel.previous
            self._count -= 1

    @property
    def empty(self) -> bool:
        """ Property to determine whether the list is empty
            @:return bool whether the list is empty
        """
        return self._count == 0

    def remove_first(self):
        """ Remove the first item in the linked list
            Usage: linked_list.remove_first()
            @:raises IndexError if the list is empty
        """
        if self.empty:
            raise IndexError('LinkedList is empty')

        self._head = self._head.next
        self._count -= 1

    def remove_last(self):
        """ Remove the last item in the linked list
            Usage: linked_list.remove_last()
            @:raises IndexError if the list is empty
        """
        if self.empty:
            raise IndexError('LinkedList is empty')

        self._tail = self._tail.previous
        self._count -= 1

    def __contains__(self, item) -> bool:
        """ Equality operator ==
            Usage: if item in linked_list:
            @:param item the item to search for
            @:return true if the linked list contains the item
        """
        travel = self._head

        while travel is not None:
            if travel.item == item:
                return True
            else:
                travel = travel.next

        return False

    def __eq__(self, other) -> bool:
        """ Equality operator ==
            Usage: list1 == list2
            @:param other the instance to compare self to
            @:return true if the lists are equal (deep check)
        """
        if not isinstance(other, LinkedList):
            return False

        if len(other) != self._count:
            return False

        travel1 = self._head
        travel2 = other.head

        while travel1 is not None:
            if travel1.item != travel2.item:
                return False
            else:
                travel1 = travel1.next
                travel2 = travel2.next

        return True

    def __len__(self) -> int:
        """ len operator for getting length of the linked list
            Usage: size = len(linked_list)
            @:return the length of the LinkedList
        """
        return self._count

    def __iter__(self):
        """ Iterator operator (head to tail order)
            Usage: for item in LinkedList:
            @:return yields the item at ListNode
        """
        travel = self._head

        while travel is not None:
            yield travel._item
            travel = travel.next

    def __reversed__(self):
        """ Iterator Reversed operator (tail to head order)
            Usage: for item in LinkedList:
            @:return yields the item at ListNode
        """
        travel = self._tail

        while travel is not None:
            yield travel._item
            travel = travel.previous

    def __str__(self) -> str:
        """ Return a string representation of the data and structure
            Usage: print(linked_list):
            @:return str the string representation of the data and structure
        """
        string = ''

        travel = self._head

        while travel is not None:
            string = string + '[' + str(travel.item) + ']'
            travel = travel.next

        return string

    '''
    Extra Code
    # self._head = None
        #
        # self._tail = None
        #
        # self._count = None
        
    
    # self._count = None
    
    # new_node.previous = travel.previous
            #
            # new_node.next = travel
            #
            # travel.previous.next = new_node
            #
            # travel.previous = new_node
            #
            # self._count += 1
        # if travel == self._tail:
        #     new_node = ListNode(new_item, travel.previous, travel)
        #     new_node.next = travel
        #
        #     travel.previous.next = new_node
        #
        #     new_node.previous = travel.previous
        #
        #     travel.previous = new_node
        #
        #     self._count += 1

    
    '''
