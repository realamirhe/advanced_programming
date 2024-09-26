def knapsack_branch_and_bound(
    weights: list[int], values: list[int], capacity: int
) -> int:
    """
    Function to solve the 0/1 Knapsack Problem using the Branch and Bound approach.

    The 0/1 Knapsack problem involves selecting items with given weights and values to maximize the total value
    without exceeding the knapsack's capacity. In the Branch and Bound approach, the search space is explored
    by branching into including or excluding an item, and bounding is used to prune suboptimal branches based
    on an upper bound of the maximum value achievable from that state.

    Args:
    weights (list[int]): A list of integers representing the weights of the items.
    values (list[int]): A list of integers representing the values of the items.
    capacity (int): The maximum capacity of the knapsack.

    Returns:
    int: The maximum total value achievable within the given knapsack capacity.

    Time Complexity:
    - O(2^n) in the worst case, but the Branch and Bound approach significantly prunes the search space.

    Space Complexity:
    - O(n) for storing the state of each node in the priority queue.

    Example:
    >>> weights = [2, 3, 4, 5]
    >>> values = [3, 4, 5, 6]
    >>> capacity = 5
    >>> knapsack_branch_and_bound(weights, values, capacity)
    7  # Maximum total value for the given capacity
    """
    ...
