from adts.linked_list import LinkedList


class ListQueue:
    """ Class ListQueue - representing a queue based on a LinkedList
            Stipulations:
            1. Must use a LinkedList as the internal data structure from the LinkedList assignment.
            2. Must adhere to the docstring requirements per method, including raising
               raising appropriate exceptions where indicated.
            3. Must achieve a minimum of 92% code coverage through unit testing.
    """

    def __init__(self, instance=None) -> None:
        """ Constructor
            Usage:  queue = ListQueue()
            @:param instance an optional ListQueue instance to deep copy data from.
            @:return none
            @:raises TypeError if instance is provided and it is not an ListQueue instance
        """
        self._queue = LinkedList()
        self._front = 0

        if instance is not None:
            if not isinstance(instance, ListQueue):
                raise TypeError('Instance is not an ListQueue instance')

            self._queue = LinkedList(instance=instance._queue)

    @staticmethod
    def clone(instance):
        """ Clone the queue
            Usage:  queue = ListQueue.clone(instance)
            @:param instance an ListQueue instance to deep copy data from.
            @:return a deep object copy of the queue
            @:raises TypeError if instance is provided and it is not an ListQueue instance
        """
        if instance is not None:
            if not isinstance(instance, ListQueue):
                raise TypeError('Instance is not an ListQueue instance')

        return ListQueue(instance=instance)

    def enqueue(self, item):
        """ Enqueue an item onto the queue
            Usage:   queue.enqueue(item)
            @:param item to enqueue
            @:return none
        """
        self._queue.prepend(item)

        self._front += 1

    def dequeue(self):
        """ Dequeue an item from the queue and return the item
            Usage:   item = queue.dequeue()
            @:return item that is dequeued
            @:raises IndexError if the queue is empty
        """
        if self.empty:
            raise IndexError('Queue is empty')

        item = self._queue.first
        self._queue.remove_first()

        self._front -= 1

        return item

    def clear(self) -> None:
        """ Clear the queue
            Usage: array_queue.clear():
            @:return none
        """
        self._queue.clear()

    @property
    def front(self):
        """ Get the item at the front of the queue
            Usage:   item = queue.front
            @:return item that is in the front
            @:raises IndexError if the queue is empty
        """
        if self.empty:
            raise IndexError('Queue is empty')

        return self._queue.first

    @property
    def size(self) -> int:
        """ Get the size of the number of items on the queue
            Usage:   size = queue.size
            @:return size the number of items on the queue
        """
        return len(self._queue)

    @property
    def empty(self) -> bool:
        """ Check whether the queue is empty
            Usage:   empty = queue.empty
            @:return empty boolean as to whether the queue is empty
        """
        return len(self._queue) == 0

    def __eq__(self, other) -> bool:
        """ Equality operator ==
            Usage: array1 == array2
            @:param other the instance to compare self to
            @:return true if the arrays are equal (deep check)
        """
        if not isinstance(other, ListQueue):
            return False

        if len(other) != len(self._queue):
            return False

        return self._queue == other._queue

    def __len__(self) -> int:
        """ len operator for getting length of the queue
            Usage: length = len(queue)
            @:return the length of the Queue (number of items on the queue)
        """
        return len(self._queue)

    def __str__(self) -> str:
        """ Return a string representation of the data and structure
            Usage: print(queue):
            @:return str the string representation of the data and structure
        """
        return f'{str(self._queue)}'
