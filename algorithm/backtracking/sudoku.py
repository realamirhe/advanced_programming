def sudoku(board: list[list[int]]) -> bool:
    """
    Function to solve a given Sudoku puzzle using backtracking.

    Sudoku is a 9x9 grid puzzle where each row, column, and 3x3 sub-grid must contain the digits from 1 to 9
    without repetition. The backtracking approach tries to fill empty cells one by one, checking at each step
    if the placement is valid. If an invalid placement is encountered, it backtracks and tries a different number.

    Args:
    board (list[list[int]]): A 9x9 list representing the Sudoku puzzle, where empty cells are denoted by 0.

    Returns:
    bool: True if the Sudoku puzzle is solvable, otherwise False. The board is modified in-place to represent the solution.

    Time Complexity:
    - O(9^m), where `m` is the number of empty cells, since there are 9 possibilities for each empty cell.

    Space Complexity:
    - O(1) as the board is modified in-place and only recursion stack space is used.

    Example:
    >>> board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    >>> sudoku(board)
    True  # The board is solved in-place
    """
    ...
