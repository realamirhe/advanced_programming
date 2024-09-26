def solve_n_queens(n: int) -> list[list[str]]:
    """
    Function to solve the N-Queens problem using backtracking.

    The N-Queens problem involves placing N queens on an N x N chessboard such that no two queens threaten each other.
    A queen can attack any other queen in the same row, column, or diagonal. The goal is to find all possible
    configurations where the queens can be placed without attacking each other.

    Args:
    n (int): The number of queens to place on the N x N chessboard.

    Returns:
    list[list[str]]: A list of all valid solutions. Each solution is represented as a list of strings,
                     where '.' represents an empty space and 'Q' represents a queen.

    Time Complexity:
    - O(n!) due to the nature of backtracking and trying all possible configurations.

    Space Complexity:
    - O(n^2) for storing the board and results.

    Example:
    >>> n = 4
    >>> solve_n_queens(n)
    [['.Q..', '...Q', 'Q...', '..Q.'],
     ['..Q.', 'Q...', '...Q', '.Q..']]
    # Two valid solutions for 4-Queens problem
    """
    ...
