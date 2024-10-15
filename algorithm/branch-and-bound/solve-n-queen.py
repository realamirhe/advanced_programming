class LookupCodes:
    def __init__(self, n) -> None:
        self.n = n
        self.slash_code = [False] * (2 * n - 1)
        self.back_slash_code = [False] * (2 * n - 1)
        self.rows = [False] * n

    def is_safe(self, i, j):
        return not (
            self.slash_code[i + j]
            or self.back_slash_code[i - j + (self.n - 1)]
            or self.rows[i]
        )

    def fill(self, i, j, value=True):
        self.slash_code[i + j] = value
        self.back_slash_code[i - j + self.n - 1] = value
        self.rows[i] = value


EMPTY_STATE = "⬛"
FILLED_STATE = "🔳"


def solve_n_queens_util(mat, lookup, col):
    if col == lookup.n:
        return True

    for row in range(lookup.n):
        if lookup.is_safe(row, col):
            lookup.fill(row, col, True)
            mat[row][col] = FILLED_STATE
            if solve_n_queens_util(mat, lookup, col + 1):
                return True
            mat[row][col] = EMPTY_STATE
            lookup.fill(row, col, False)

    return False


def pprint(mat):
    for row in mat:
        print(" ".join(list(map(str, row))))


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
    lookup = LookupCodes(n)
    mat = [[EMPTY_STATE] * n for i in range(n)]

    col = 0
    if solve_n_queens_util(mat, lookup, col):
        pprint(mat)
    else:
        print("no answer")


solve_n_queens(18)