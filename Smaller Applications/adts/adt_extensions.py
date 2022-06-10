from adts.array import Array
from adts.array_stack import ArrayStack
from adts.circular_array_queue import CircularArrayQueue
from adts.linked_list import LinkedList
from adts.list_queue import ListQueue
from adts.list_stack import ListStack


def extends(klass):
    """ Custom Python decorator to extend a Python class
        with additional methods outside of the class
        Note: you don't need to change this method
    """
    def decorator(func):
        setattr(klass, func.__name__, func)
        return func

    return decorator


@extends(Array)
def to_reversed_array(self: Array):
    """ Extension method to return a reversed array
        Usage: reversed_array = array.to_reversed_array()
        @:param none
        @:return reversed_array an Array with the items in the reversed order
    """
    reversed_array = self[::-1]

    return reversed_array


@extends(Array)
def to_linked_list(self: Array) -> LinkedList:
    """ Extension method to convert an Array to a LinkedList
        Usage: linked_list = array.to_linked_list()
        @:param none
        @:return linked_list a LinkedList containing the items from the array in the same order
    """
    linked_list = LinkedList()

    for i in range(len(self)):
        linked_list.append(self[i])

    return linked_list


@extends(LinkedList)
def to_array(self: LinkedList) -> Array:
    """ Extension method to convert a LinkedList to an Array
        Usage: array = linked_list.to_array()
        @:param none
        @:return array an Array containing the items from the linked list in the same order
    """
    array = Array(len(self))

    i = 0

    travel = self.head
    while travel is not None:
        array[i] = travel.item
        i += 1
        travel = travel.next

    return array


@extends(CircularArrayQueue)
def to_list_queue(self: CircularArrayQueue) -> ListQueue:
    """ Extension method to CircularArrayQueue to a ListQueue
        Usage: list_queue = circular_array_queue.to_list_queue()
        @:param none
        @:return list_queue a ListQueue containing the items from the CircularArrayQueue in the same order
    """
    list_queue = ListQueue()

    for i in range(len(self)):
        list_queue.enqueue(self.dequeue())

    return list_queue


@extends(ListQueue)
def to_circular_array_queue(self: ListQueue):
    """ Extension method to convert a ListQueue to a CircularArrayQueue
        Usage: circular_array_queue = list_queue.to_circular_array_queue()
        @:param none
        @:return array_queue a CircularArrayQueue containing the items from the ListQueue in the same order
    """
    array_queue = CircularArrayQueue(self.size)

    for i in range(self.size):
        item = self.dequeue()
        array_queue.enqueue(item)

    return array_queue


@extends(ArrayStack)
def to_list_stack(self: ArrayStack):
    """ Extension method to convert an ArrayStack to a ListStack
        Usage: list_stack = array_stack.to_list_stack()
        @:param none
        @:return list_stack a ListStack containing the items from the ArrayStack i in the same order
    """
    list_stack = ListStack()

    for i in range(len(self)):
        list_stack.push(self.pop())

    return list_stack


@extends(ListStack)
def to_array_stack(self: ListStack):
    """ Extension method to convert a ListStack to an ArrayStack
        Usage: list_stack = array_stack.to_list_stack()
        @:param none
        @:return array_stack a ArrayStack containing the items from the ListStack i in the same order
    """
    array_stack = ArrayStack(len(self))

    for i in range(len(self)):
        array_stack.push(self.pop())

    return array_stack


# Example usages
my_array = Array(10)
for i in range(10):
    my_array[i] = i

print(f'Starting with Array: {my_array}')

# Array to LinkedList
linked_list = my_array.to_linked_list()
print(f'Converting Array: {my_array} to LinkedList: {linked_list}')

# Reverse Array
reversed_array = my_array.to_reversed_array()
print(f'Reversed Array: {reversed_array}')

# LinkedList to Array
my_array = linked_list.to_array()
print(f'Converting the LinkedList:{linked_list} back to Array: {my_array}')

# CircularArrayQueue to ListQueue
array_queue = CircularArrayQueue(10)
for i in my_array:
    array_queue.enqueue(i)

list_queue: ListQueue = array_queue.to_list_queue()
print(
    f'Enqueueing the array elements into CircularArrayQueue {array_queue} and converting it to a ListQueue: {list_queue}')

# ListQueue to CircularArrayQueue
array_queue: CircularArrayQueue = list_queue.to_circular_array_queue()
print(f'Converting the ListQueue: {list_queue} back to an CircularArrayQueue: {array_queue}')

# ArrayStack to ListStack
array_stack = ArrayStack(10)
for i in my_array:
    array_stack.push(i)

list_stack = array_stack.to_list_stack()
print(f'Converting ArrayStack: {array_stack} to a ListStack: {list_stack}')

# ListStack to ArrayStack
array_stack = list_stack.to_array_stack()
print(f'Converting the ListStack: {list_stack} back to an ArrayStack: {array_stack}')
