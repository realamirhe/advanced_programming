def subset_sum(nums: list[int], target: int) -> list[list[int]]:
    """
    Function to solve the Subset Sum problem using backtracking.

    The Subset Sum problem involves finding all subsets of a given set of integers `nums` that sum up to a target value.
    The backtracking approach explores all possible subsets by including or excluding each number and checks if the sum
    of a subset equals the target value.

    Args:
    nums (list[int]): A list of integers representing the set of numbers.
    target (int): The target sum we want to achieve with a subset of `nums`.

    Returns:
    list[list[int]]: A list of all subsets whose sum equals the target. Each subset is represented as a list of integers.

    Time Complexity:
    - O(2^n), where `n` is the number of elements in `nums`, since all subsets are explored.

    Space Complexity:
    - O(n) for storing the current subset during the recursion.

    Example:
    >>> nums = [3, 34, 4, 12, 5, 2]
    >>> target = 9
    >>> subset_sum(nums, target)
    [[3, 4, 2], [4, 5]]  # Two subsets that sum to 9
    """
    ...
