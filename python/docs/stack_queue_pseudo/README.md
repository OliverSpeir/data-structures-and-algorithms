# Challenge Summary
Create a new class called pseudo queue.
Do not use an existing Queue.
Instead, this PseudoQueue class will implement our standard queue interface (the two methods listed below),
Internally, utilize 2 Stack instances to create and manage the queue

## Whiteboard Process

![Stack Queue Whiteboard](/python/docs/stack_queue_pseudo/Psuedo_Queue_WB.png)

## Approach & Efficiency
Approach: rotate items between two stacks in order to reverse their order so to be able to push to top and return the "last" item in stack which should be first to be dequeued
Efficiency: O(n) has will need to go through entire list every time

## Solution
- `pytest ./tests/code_challenges/test_stack_queue_pseudo.py`
- This runs the tests for the code
- This code is not set up to be run as main

## Files
- [code](../../code_challenges/stack_queue_pseudo.py)
- [tests](../../tests/code_challenges/test_stack_queue_pseudo.py)
