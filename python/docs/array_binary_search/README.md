# Problem Description
Write a function called BinarySearch which takes in 2 parameters: a sorted array and the search key.
Without utilizing any of the built-in methods available to your language, return the index of the array’s
element that is equal to the value of the search key, or -1 if the element is not in the array.

## Whiteboard Process

![array_binary_search](/python/docs/array_insert_shift/array_binary_search.png)

## Approach & Efficiency
- Determine length of array (built into python)
- Divide length by 2 (rounding up)
- Search first half for value
- Search second half for value
- return -1 if value is not in array or the position of the value in array
