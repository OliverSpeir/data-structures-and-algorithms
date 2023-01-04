# Challenge Summary
Create a class called AnimalShelter which holds only dogs and cats.
The shelter operates using a first-in, first-out approach.
Implement the following methods:
- enqueue
  - Arguments: animal
    - animal can be either a dog or a cat object.
  - dequeue
    - Arguments: pref
    - pref can be either "dog" or "cat"
     - Return: either a dog or a cat, based on preference.
    - If pref is not "dog" or "cat" then return null.

## Whiteboard Process
![whiteboard](/python/docs/stack_queue_animal_shelter/queue_animal_shelter.png)

## Approach & Efficiency
Approach: Queue that conditionally dequeues the top value. If top = passed value then pop else iterate to next node
Efficiency: O(n) as it will need to iterate through the list O(n) space as it will need to allocate memory for every animal in shelter

## Solution
- `pytest ./tests/code_challenges/test_stack_queue_animal_shelter.py`
- This runs the tests for the code
- This code is not set up to be run as main at the moment

## Files
- [code](../../code_challenges/stack_queue_animal_shelter.py)
- [tests](../../tests/code_challenges/test_stack_queue_animal_shelter.py)
