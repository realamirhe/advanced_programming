def merge_sort(arr: list[int]) -> list[int]:
    """
    Function to perform Merge Sort on a given list of integers.

    Merge Sort is a divide-and-conquer algorithm that recursively splits the input list into two halves,
    sorts each half, and then merges the two sorted halves to produce the final sorted list.

    Args:
    arr (list[int]): The input list of integers to be sorted.

    Returns:
    list[int]: A new list containing the sorted elements from the input list.

    Time Complexity:
    - O(n log n), where `n` is the number of elements in the list.

    Space Complexity:
    - O(n) for the additional space needed to merge the sorted halves.

    Example:
    >>> arr = [38, 27, 43, 3, 9, 82, 10]
    >>> merge_sort(arr)
    [3, 9, 10, 27, 38, 43, 82]  # Sorted list
    """
    ...
