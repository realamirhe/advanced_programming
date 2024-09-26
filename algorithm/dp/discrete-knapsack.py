def knapsack_01(items: list[tuple[int, int]], capacity: int) -> int:
    """
    Function to solve the 0-1 Knapsack Problem using dynamic programming.

    The 0-1 Knapsack Problem aims to determine the maximum value that can be obtained from a set of items
    with given weights and values, such that the total weight does not exceed the given capacity.
    In this version of the problem, you either take the whole item (1) or leave it (0), no fractions allowed.

    Args:
    items (list[tuple[int, int]]): A list of items, where each item is represented as a tuple (value, weight).
        - value (int): The value of the item.
        - weight (int): The weight of the item.
    capacity (int): The maximum capacity (weight) that the knapsack can hold.

    Returns:
    int: The maximum value that can be obtained by selecting items without exceeding the capacity.

    Time Complexity:
    - O(n * capacity), where `n` is the number of items and `capacity` is the knapsack capacity.

    Space Complexity:
    - O(n * capacity) for the 2D table used to store results of subproblems.

    Example:
    >>> items = [(3, 2), (4, 3), (5, 4), (6, 5)]
    >>> capacity = 5
    >>> knapsack_01(items, capacity)
    7  # Maximum value that can be obtained is 7
    """
    ...
