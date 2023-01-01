from python.data_structures.invalid_operation_error import InvalidOperationError


class Node:
    def __init__(self, value=None, nextval=None):
        self.value = value
        self.next = nextval

class Queue:
    """
    Put docstring here
    """

    def __init__(self):
        self.front = None
        self.back = None

    def enqueue(self, value):
        if self.back:
            self.back.next = Node(value)
            self.back = self.back.next
            return
        self.back = self.front = Node(value)

    def dequeue(self):
        try:
            dequeued = self.front
            self.front = self.front.next
            return dequeued.value
        except Exception as e:
            raise InvalidOperationError("Method not allowed on empty collection")

    def peek(self):
        try:
            return self.front.value
        except Exception as e:
            raise InvalidOperationError("Method not allowed on empty collection")

    def is_empty(self):
        return self.front is None
