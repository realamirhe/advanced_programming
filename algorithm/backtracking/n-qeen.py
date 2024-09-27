def n_queens(n: int) -> list[list[str]]:
    """
    Function to solve the N-Queens problem using a backtracking approach.

    The N-Queens problem requires placing N queens on an N x N chessboard such that no two queens threaten each other.
    This means no two queens can share the same row, column, or diagonal. The backtracking approach attempts to place
    queens one row at a time and backtracks if a conflict occurs.

    Args:
    n (int): The number of queens (and the size of the N x N chessboard).

    Returns:
    list[list[str]]: A list of all valid solutions. Each solution is represented as a list of strings,
                     where '.' represents an empty square and 'Q' represents a queen.

    Time Complexity:
    - O(n!) due to the recursive nature of backtracking for N queens.

    Space Complexity:
    - O(n^2) for storing the chessboard and results.

    Example:
    >>> n_queens(4)
    [['.Q..', '...Q', 'Q...', '..Q.'],
     ['..Q.', 'Q...', '...Q', '.Q..']]  # Two valid solutions for 4-Queens problem
    """
    ...
