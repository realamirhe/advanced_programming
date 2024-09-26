def binary_search(arr: list[int], target: int) -> int:
    """
    Function to perform Binary Search on a sorted list of integers.

    Binary Search is an efficient algorithm for finding the position of a target value within a sorted list.
    It works by repeatedly dividing the search interval in half. If the target value is equal to the middle
    element, the search is successful. If the target is smaller, the search continues in the left half,
    otherwise in the right half.

    Args:
    arr (list[int]): The sorted list of integers to search in.
    target (int): The integer value to search for.

    Returns:
    int: The index of the target value if found, otherwise -1.

    Time Complexity:
    - O(log n), where `n` is the number of elements in the list.

    Space Complexity:
    - O(1) for the iterative approach or O(log n) for the recursive approach.

    Example:
    >>> arr = [1, 2, 3, 4, 5, 6, 7]
    >>> target = 4
    >>> binary_search(arr, target)
    3  # Index of target in the list
    """
    ...
