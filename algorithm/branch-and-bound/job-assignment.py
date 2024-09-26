def job_assignment(cost_matrix: list[list[int]]) -> int:
    """
    Function to solve the Job Assignment Problem using a dynamic programming or backtracking approach.

    The Job Assignment Problem involves assigning jobs to workers such that each worker is assigned exactly one job,
    and the total cost of the assignments is minimized. The cost of assigning job `j` to worker `i` is given by
    `cost_matrix[i][j]`. The goal is to find the assignment that results in the minimum total cost.

    Args:
    cost_matrix (list[list[int]]): A 2D list where `cost_matrix[i][j]` represents the cost of assigning job `j` to worker `i`.

    Returns:
    int: The minimum cost of assigning all jobs to the workers.

    Time Complexity:
    - O(n * 2^n) for the dynamic programming approach with bit-masking, where `n` is the number of workers/jobs.

    Space Complexity:
    - O(2^n) for the DP table or recursion stack.

    Example:
    >>> cost_matrix = [[9, 2, 7, 8], [6, 4, 3, 7], [5, 8, 1, 8], [7, 6, 9, 4]]
    >>> job_assignment(cost_matrix)
    13  # Minimum cost of assigning jobs
    """
    ...
