import sys


def matrix_chain_multiplication(
    dims: list[int],
    i,
    j,
    memo: dict[tuple[int, int], int],
) -> int:
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

    Preview: https://www.mimuw.edu.pl/~erykk/algovis/mcm.html
    Example:
    # 5x5 5x4 4x8 => 5x8
    >>> dims = [5, 5, 4, 8]
    >>> matrix_chain_multiplication(dims)
    260  # Minimum number of scalar multiplications needed
    """

    if i + 1 == j:
        return 0

    if (memoized := memo.get((i, j), None)) is not None:
        return memoized

    result = sys.maxsize
    beg = dims[i]
    end = dims[j]

    for k in range(i + 1, j):
        result = min(
            result,
            matrix_chain_multiplication(dims, i, k, memo)
            + matrix_chain_multiplication(dims, k, j, memo)
            + beg * dims[k] * end,
        )

    memo[(i, j)] = result
    return result


dims = [5, 5, 4, 8]
print(
    matrix_chain_multiplication(
        dims,
        i=0,
        j=len(dims) - 1,
        memo={},
    )
)