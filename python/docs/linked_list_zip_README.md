# Challenge Summary
merge two lists, one value from list 1 then the next value from list 2... creating a "zipper" effect

## Whiteboard Process
<img src = "https://i.imgur.com/i2BT8lf.png"/>

## Approach & Efficiency
Approach: create two pointers for each list added, then iterate through both at the same time. Each iteration put the head value list b on the next value of list a's current node then reset the head of list b to its current position.
          if there is a next value in list a put it as the head of list b otherwise the head will stay as b's current position.

          list b will be erase and list a will be mutated

Efficiency: O(1) as the pointers are just being rearranged no new memory is allocated

## Solution
- `pytest ./tests/code_challenges/test_linked_list_insertions.py`
- This runs the tests for the code
- This code is not set up to be run as main at the moment

## Files
- [code](../code_challenges/linked_list_zip.py)
- [tests](../tests/code_challenges/test_linked_list_zip.py)
