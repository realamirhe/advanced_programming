def matrix_chain_multiplication(dims: list[int]) -> int:
    """
    Function to solve the Matrix Chain Multiplication problem using dynamic programming.

    The Matrix Chain Multiplication problem aims to find the most efficient way to multiply a sequence of matrices
    (i.e., to determine the order of matrix multiplications that minimizes the total number of scalar multiplications).
    The dimensions of the matrices are given in a list, where the i-th matrix has dimensions dims[i-1] x dims[i].

    Args:
    dims (list[int]): A list of dimensions of the matrices, where matrix i has dimensions dims[i-1] x dims[i].

    Returns:
    int: The minimum number of scalar multiplications needed to multiply the matrices.

    Time Complexity:
    - O(n^3), where `n` is the number of matrices (length of dims - 1).

    Space Complexity:
    - O(n^2) for the 2D table to store the results of subproblems.

    Example:
    >>> dims = [1, 2, 3, 4]
    >>> matrix_chain_multiplication(dims)
    18  # Minimum number of scalar multiplications needed
    """
    ...
