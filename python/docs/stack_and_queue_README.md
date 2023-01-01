# Stacks and Queues
- Stack: LinkedList that functions like a stack, only knows its head value and can return its head value, remove from head or add to head
- Queue: LinkedLIst that functions like a queue, only knows its head and tail value, can return its head value, remove from head and add to tail, removing returns the value of node removed

## Challenge
Create both of these structures with their appropriate  methods and error handling for both

## Approach & Efficiency
These structures function O(1) for time and O(n) for space
They are O(1) for time because they only work with positions in the list that are known without having to traverse

## API
Stack Methods:
  - push
    - adds to head
  - pop
    - removes from head and returns value of node removed
  - peek
    - returns value of head
  - is_empty
    - returns boolean if head is not None

Queue Methods:
  - enqueue
    - adds to tail of list
  - dequeue
    - removes from head of list and returns the value the removed node
  - peek
    - returns head value
  - is_empty
    - returns boolean if head is not None


## Code and Tests
- [queue code](../data_structures/queue.py)
- [stack code](../data_structures/stack.py)
- [queue tests](../tests/data_structures/test_queue.py)
- [stack tests](../tests/data_structures/test_stack.py)
