## Merge Sort

1. If the list has 1 or 0 elements, it is already sorted.
2. Recursively split the list into two halves.
3. Recursively sort each half using merge sort.
4. Merge the two sorted halves into a single sorted list.

## Binary Search

1. Initialize two pointers, `low` and `high`, pointing to the start and end of the list.
2. While `low` is less than or equal to `high`, compute the middle index.
3. If the target is equal to the middle element, return the middle index.
4. If the target is less than the middle element, update `high` to search the left half.
5. If the target is greater than the middle element, update `low` to search the right half.
6. If the target is not found, return -1.
