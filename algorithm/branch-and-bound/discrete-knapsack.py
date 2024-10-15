from __future__ import annotations


class Item:
    __slots__ = ["weight", "value", "scale"]

    def __init__(self, weight: float, value: float) -> None:
        self.weight = weight
        self.value = value
        self.scale = self.value / self.weight

    def __repr__(self) -> str:
        return f"(w={self.weight},v={self.value})"

    def __lt__(self, other: Item) -> bool:
        return self.scale < other.scale


class Node:
    __slots__ = ["index", "weight", "bound", "profit"]

    def __init__(self, /, *, profit, weight, index):
        self.index = index
        self.profit = profit
        self.weight = weight
        self.bound = None  # will be bound to the fractional_knapsack (greedy)

    def __repr__(self) -> str:
        return f"{self.index}(p={self.profit}, w={self.weight}, b={self.bound})"


def fractional_knapsack(items: list[Item], capacity: int) -> float:
    items.sort(key=lambda item: item.scale, reverse=True)
    result = 0

    for item in items:
        if capacity == 0:
            break
        take_over = min(capacity, item.weight)
        result += take_over * item.scale
        capacity -= take_over

    return result


def knapsack_branch_and_bound(items: list[Item], capacity: int) -> int:
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

    items.sort(reverse=True)
    print(items)
    n = len(items)
    queue = [Node(profit=0, weight=0, index=0)]
    max_profit = 0

    while queue:
        node = queue.pop(0)
        print(node)

        # next_item_included_node
        child = Node(
            profit=node.profit + items[node.index].value,
            weight=node.weight + items[node.index].weight,
            index=node.index + 1,
        )

        if child.weight <= capacity and child.profit >= max_profit:
            max_profit = child.profit

        child.bound = fractional_knapsack(
            items=items[child.index :],
            capacity=capacity - child.weight,
        )

        if child.bound > max_profit:
            queue.append(child)

        # next_item_excluded_node
        child = Node(
            profit=node.profit,
            weight=node.weight,
            index=node.index + 1,
        )
        child.bound = fractional_knapsack(
            items=items[child.index :],
            capacity=capacity - child.weight,
        )
        if child.bound > max_profit:
            queue.append(child)

    return max_profit


items = [
    Item(weight=2, value=40),
    Item(weight=3.14, value=50),
    Item(weight=1.98, value=100),
    Item(weight=5, value=95),
    Item(weight=3, value=30),
]
profit = knapsack_branch_and_bound(items=items, capacity=10)
print(profit)
