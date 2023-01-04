# Challenge Summary
Write a function called validate brackets
Arguments: string
Return: boolean
representing whether or not the brackets in the string are balanced

## Whiteboard Process
![whiteboard](/python/docs/stack_queue_brackets/brackets_WB.png)

## Approach & Efficiency
Approach: Use a for loop to go over entire string and a stack to hold any brackets in a stack, then pop from the stack if there is a closing bracket. Return false if the stack is not empty at end.
Efficiency: O(n) as it will need to go over entire input string is variable length
## Solution
- `pytest ./tests/code_challenges/test_stack_queue_backets.py`
- This runs the tests for the code
- This code is not set up to be run as main at the moment

## Files
- [code](../../code_challenges/stack_queue_brackets.py)
- [tests](../../tests/code_challenges/test_stack_queue_brackets.py)
