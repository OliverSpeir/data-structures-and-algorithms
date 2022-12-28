# Challenge Summary
Add method to return the kth value from the last item in the list

## Whiteboard Process
<img src = "https://i.imgur.com/S0dlcSV.png"/>

## Approach & Efficiency
Approach: iterate through list and create length of list then iterate through the list again until the (length - input value) position
Efficiency: O(n) has will need to go through entire list twice every time which can be improved upon

## Solution
- `pytest ./tests/code_challenges/test_linked_list_insertions.py`
- This runs the tests for the code
- This code is not set up to be run as main at the moment

## Files
- [code](../data_structures/linked_list.py)
- [tests](../tests/code_challenges/test_linked_list_kth.py)
