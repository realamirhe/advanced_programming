class Pos:
    __slots__ = ["row", "col"]

    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __add__(self, next):
        return Pos(
            row=self.row + next.row,
            col=self.col + next.col,
        )

    def __repr__(self) -> str:
        return f"pos({self.row},{self.col})"

    def set(self, board, value):
        board[self.row][self.col] = value

    def is_row_safe(self, board) -> bool:
        n = len(board)
        for j in range(n):
            if board[self.row][j]:
                return False
        return True

    def is_col_safe(self, board) -> bool:
        n = len(board)
        for i in range(n):
            if board[i][self.col]:
                return False
        return True

    def is_diagonal_safe(self, board) -> bool:
        n = len(board)
        for i, j in zip(range(self.row, -1, -1), range(self.col, -1, -1)):
            if board[i][j]:
                return False

        for i, j in zip(range(self.row, n), range(self.col, -1, -1)):
            if board[i][j]:
                return False

    def is_safe(self, board) -> bool:
        return (
            self.is_row_safe(board)
            and self.is_col_safe(board)
            and self.is_diagonal_safe(board)
        )


def pprint(tour):
    for row in tour:
        print(" ".join([f"{i: >3}" for i in row]))


def n_queen_util(board, col):
    # is there any solution
    n = len(board)
    if col == n:  # stop condition (final case)
        return True
    # recurse
    for row in range(n):
        new_pos = Pos(row, col)
        if new_pos.is_safe(board):
            new_pos.set(board, 1)
            if n_queen_util(board, col + 1):  # if it find the solution exit
                return True
            new_pos.set(board, 0)  # reset

    return False  # no answer has been found


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

    reference: https://media.geeksforgeeks.org/wp-content/uploads/20230814111826/Backtracking.png

    Example:
    >>> n_queens(4)
    [['.Q..', '...Q', 'Q...', '..Q.'],
     ['..Q.', 'Q...', '...Q', '.Q..']]  # Two valid solutions for 4-Queens problem

    # TODO: try to generate all the solution with the help of an accumulator
    """
    # initialize the state of the program
    board = [[0] * n for _ in range(n)]
    if not n_queen_util(board, 0):
        print("NO SOLUTION")
    else:
        pprint(board)


n_queens(11)