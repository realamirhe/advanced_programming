def knights_tour(n: int) -> list[list[int]]:
    """
    Function to solve the Knight's Tour problem using backtracking.

    The Knight's Tour problem involves finding a sequence of moves for a knight on an `n x n` chessboard such that
    the knight visits every square exactly once. The knight moves in an L-shape (two squares in one direction and one
    square perpendicular, or vice versa). The goal is to find a valid tour that covers the entire board.

    Args:
    n (int): The size of the chessboard (n x n).

    Returns:
    list[list[int]]: A 2D list representing the board, where each cell contains the move number in which it was visited.
                     If no solution exists, an empty list is returned.

    Time Complexity:
    - O(8^n^2), where `n` is the size of the board, since the knight can make up to 8 possible moves.

    Space Complexity:
    - O(n^2) for storing the chessboard and visited moves.

    Example:
    >>> knights_tour(5)
    [[0, 21, 2, 17, 8],
     [3, 16, 9, 22, 1],
     [10, 23, 4, 7, 18],
     [15, 6, 19, 12, 5],
     [20, 11, 14, 13, 24]]  # Solution to a 5x5 board Knight's Tour
    """
    ...
