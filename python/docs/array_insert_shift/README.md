# Problem Description
Write a function called `insertShiftArray` which takes in an array and a value to be added.
Without utilizing any of the built-in methods available to your language,
return an array with the new value added at the middle index.

## Whiteboard Process

![array_insert_shift](/python/docs/array_insert_shift/array_insert_shift.png)

## Approach & Efficiency
- Find length of array
- Divide length by 2 (rounding up)
  - Add 1 because there will be a "new middle" once our value is added
- Copy array to avoid mutating it
- Insert our value into the new array
- return the new array
