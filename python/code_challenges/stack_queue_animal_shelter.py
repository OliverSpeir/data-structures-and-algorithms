from python.data_structures.queue import Queue


class AnimalShelter:
    def __init__(self):
        self.list = Queue()

    def dequeue(self, value):
        if value != "cat" and value != "dog":
            return None
        node_to_deq = self.list.head
        previous = None
        if node_to_deq.value.value is value:
            return self.list.dequeue()
        while node_to_deq.value.value is not value:
            previous = node_to_deq
            node_to_deq = node_to_deq.next
        previous.next = node_to_deq.next
        return node_to_deq.value

    def enqueue(self, value):
        self.list.enqueue(value)


class Dog:
    def __init__(self, next_val=None):
        self.value = "dog"
        self.next = next_val


class Cat:
    def __init__(self, next_val=None):
        self.value = "cat"
        self.next = next_val
