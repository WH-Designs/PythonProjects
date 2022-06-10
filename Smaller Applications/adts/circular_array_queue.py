from adts.array import Array


class CircularArrayQueue:
    """ Class CircularArrayQueue - representing a circular array queue using a 1D Array
            Stipulations:
            1. Must use an Array object as the internal data structure.
            2. Storage must wrap-around the array.
            3. Must adhere to the docstring requirements per method, including raising
               raising appropriate exceptions where indicated.
            4. Must achieve a minimum of 92% code coverage through unit testing.
    """

    def __init__(self, max_size: int = 0, instance=None) -> None:
        """ Constructor
            Usage:  queue = CircularArrayQueue(10)
            @:param size the desired size of the queue
            @:param instance an optional CircularArrayQueue instance to deep copy data from.
            @:return none
            @:raises TypeError if instance is provided and it is not an CircularArrayQueue instance
        """
        if instance is not None:
            if not isinstance(instance, CircularArrayQueue):
                raise TypeError('Instance is not an CircularArrayQueue instance')

            self._queue = Array(instance=instance._queue)
            self._front = instance._front
            self._rear = instance._rear

        self._queue = Array(max_size + 1)
        self._front = 0
        self._rear = 0

    @staticmethod
    def clone(instance):
        """ Clone the queue
            Usage:  queue = CircularArrayQueue.clone(instance)
            @:param instance an CircularArrayQueue instance to deep copy data from.
            @:return a deep object copy of the queue
            @:raises TypeError if instance is provided and it is not an CircularArrayQueue instance
        """
        if instance is not None:
            if not isinstance(instance, CircularArrayQueue):
                raise TypeError('Instance is not an ArrayStack instance')

        return CircularArrayQueue(instance=instance)

    def enqueue(self, item):
        """ Enqueue an item onto the queue
            Usage:   queue.enqueue(item)
            @:param item to enqueue
            @:return none
            @:raises IndexError if the queue is full
        """
        if len(self._queue) == self.size - 1:
            raise IndexError('Queue is full')

        elif not self.full:
            self._queue[self._rear] = item
            self._rear = (self._rear + 1) % len(self._queue)

    def dequeue(self):
        """ Dequeue an item from the queue and return the item
            Usage:   item = queue.dequeue()
            @:return item that is dequeued
            @:raises IndexError if the queue is empty
        """
        if self.empty:
            raise IndexError('Queue is empty')

        item = self._queue[self._front]
        self._front = self._front + 1 % self.size
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

        return self._queue[self._front]

    @property
    def size(self) -> int:
        """ Get the size of the number of items on the queue
            Usage:   size = queue.size
            @:return size the number of items on the queue
        """
        return len(self._queue)

    @property
    def full(self) -> bool:
        """ Check whether the queue is full
            Usage:   full = queue.full
            @:return full boolean as to whether the queue is full
        """
        return True if len(self) + 1 == len(self._queue) else False

    @property
    def empty(self) -> bool:
        """ Check whether the queue is empty
            Usage:   empty = queue.empty
            @:return empty boolean as to whether the queue is empty
        """
        counter = 0
        for i in self._queue:
            if i is None:
                counter += 1
        return counter == len(self._queue)

    def __eq__(self, other) -> bool:
        """ Equality operator ==
            Usage: array1 == array2
            @:param other the instance to compare self to
            @:return true if the arrays are equal (deep check)
        """
        if not isinstance(other, CircularArrayQueue):
            return False

        if self.size != other.size:
            return False

        return self._queue == other._queue

    def __len__(self) -> int:
        """ len operator for getting length of the queue
            Usage: length = len(queue)
            @:return the length of the Queue (number of items on the queue)
        """
        return (self.size - self._front + self._rear) % self.size

    def __str__(self) -> str:
        """ Return a string representation of the data and structure
            Usage: print(queue):
            @:return str the string representation of the data and structure
        """
        return f'{str(self._queue)}'
