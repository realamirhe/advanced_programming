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

    def is_bound(self, n):
        return 0 <= self.row < n and 0 <= self.col < n

    def get(self, tour):
        return tour[self.row][self.col]

    def set(self, tour, value):
        tour[self.row][self.col] = value

    def is_filled(self, tour):
        return self.get(tour) != -1

    def is_safe_for(self, tour):
        n = len(tour)
        return self.is_bound(n) and not self.is_filled(tour)


def pprint(tour):
    for row in tour:
        print(" ".join([f"{i: >3}" for i in row]))


possible_moves = [
    Pos(1, 2),
    Pos(-1, 2),
    Pos(1, -2),
    Pos(-1, -2),
    Pos(2, 1),
    Pos(2, -1),
    Pos(-2, 1),
    Pos(-2, -1),
]


def knight_tour_util(tour, current_pos, counter):
    # is there any solution
    n = len(tour)
    if counter == n**2:  # stop condition (final case)
        return True
    # recurse
    for move in possible_moves:
        new_pos = current_pos + move
        if new_pos.is_safe_for(tour):
            new_pos.set(tour, counter)
            if knight_tour_util(tour, new_pos, counter + 1):  # if solution then exit
                return True
            new_pos.set(tour, -1)  # reset

    return False  # no answer has been found


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
    - O(8^(n^2)), where `n` is the size of the board, since the knight can make up to 8 possible moves.

    Space Complexity:
    - O(n^2) for storing the chessboard and visited moves.

    Example:
    >>> knights_tour(8)
    0  59  38  33  30  17   8  63
    37  34  31  60   9  62  29  16
    58   1  36  39  32  27  18   7
    35  48  41  26  61  10  15  28
    42  57   2  49  40  23   6  19
    47  50  45  54  25  20  11  14
    56  43  52   3  22  13  24   5
    51  46  55  44  53   4  21  12
    """
    # initialize the state of the program
    tour = [[-1] * n for i in range(n)]
    current_pos = Pos(0, 0)
    current_pos.set(tour, 0)  # set current_pos in the tour for as first location
    if not knight_tour_util(tour, current_pos, 1):
        print("NO SOLUTION")
    else:
        pprint(tour)


knights_tour(6)
