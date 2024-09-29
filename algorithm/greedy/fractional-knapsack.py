class Item:
    def __init__(self, weight, value) -> None:
        self.weight = weight
        self.value = value
        self.scale = self.value / self.weight

    def __repr__(self) -> str:
        return f"(w={self.weight},v={self.value})"


def fractional_knapsack(items: list[Item], capacity: int) -> float:
    """
    Function to solve the Fractional Knapsack Problem using a greedy algorithm.

    The Fractional Knapsack Problem is aimed at maximizing the total value in the knapsack by selecting items
    such that the total weight does not exceed the given capacity. Unlike the 0/1 knapsack problem, you can take
    fractions of an item.

    Args:
    items (list[Item]): A list of items, where each item is represented as a tuple (value, weight).
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
    items.sort(key=lambda item: item.scale, reverse=True)
    result = 0

    for item in items:
        if capacity == 0:
            break
        take_over = min(capacity, item.weight)
        result += take_over * item.scale
        capacity -= take_over

    return result


items = [
    Item(weight=10, value=60),
    Item(weight=20, value=100),
    Item(weight=30, value=120),
]


print(
    fractional_knapsack(
        items=items,
        capacity=50,
    )
)