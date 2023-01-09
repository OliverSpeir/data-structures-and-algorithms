# Trees
Trees are common data structure with a wealth of literature about them

## Challenge
Create Binary Tree and Binary Search Tree classes, binary tree needs all DFT methods and BST needs contains and add method

## Approach & Efficiency
- Depth first traversal methods have O(n) for time and space
- binary_search_tree has O(log n) for time and O(n) for space

## API
- binary_tree has:
  - pre_order
    - Depth First Traversal, Search method that returns list of values in tree, according to pre-order convention
  - in_order
    - Depth First Traversal, Search method that returns list of values in tree, according to in_order convention
  - post_order
    - Depth First Traversal, Search method that returns list of values in tree, according to pst_order convention
- binary_search_tree has:
  - add
    - adds node in correct place within tree according to binary search tree conventions
  - contains
    - returns boolean if value exists in tree
