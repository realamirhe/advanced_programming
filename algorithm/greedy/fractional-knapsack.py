def fractional_knapsack(items: list[tuple[int, int]], capacity: int) -> float:
    """
    Function to solve the Fractional Knapsack Problem using a greedy algorithm.

    The Fractional Knapsack Problem is aimed at maximizing the total value in the knapsack by selecting items
    such that the total weight does not exceed the given capacity. Unlike the 0/1 knapsack problem, you can take
    fractions of an item.

    Args:
    items (list[tuple[int, int]]): A list of items, where each item is represented as a tuple (value, weight).
        - value (int): The value of the item.
        - weight (int): The weight of the item.
    capacity (int): The maximum capacity (weight) the knapsack can hold.

    Returns:
    float: The maximum value that can be obtained by selecting items or fractions of items.

    Time Complexity:
    - O(n log n) due to sorting the items based on value-to-weight ratio.

    Space Complexity:
    - O(n) for storing the sorted items and the fractions of items chosen.

    Example:
    >>> items = [(60, 10), (100, 20), (120, 30)]
    >>> capacity = 50
    >>> fractional_knapsack(items, capacity)
    240  # Maximum value that can be obtained

    HINT: https://www.geeksforgeeks.org/fractional-knapsack-problem/
    Companies: Microsoft
    """
    ...
