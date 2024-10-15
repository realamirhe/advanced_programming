from __future__ import annotations

import copy
import heapq as hq


class Pos:
    __slots__ = ["i", "j"]

    def __init__(self, row: int, col: int):
        self.i = row
        self.j = col

    def __add__(self, other: Pos):
        assert isinstance(other, Pos), f"{other} must be instance of Pos"
        return Pos(self.i + other.i, self.j + other.j)

    def __sub__(self, other: Pos):
        assert isinstance(other, Pos), f"{other} must be instance of Pos"
        return Pos(self.i - other.i, self.j - other.j)

    def is_safe(self, n: int):
        return 0 <= self.i < n and 0 <= self.j < n


class Node:
    __slots__ = ["parent", "state", "pos", "cost", "final", "level"]

    def __init__(
        self,
        /,
        *,
        parent: Node,
        state: list[list[int]],
        final: list[list[int]],
        pos: Pos,
    ):
        self.parent = parent
        self.state = state
        self.final = final
        self.pos = pos  # position for zero
        self.level = parent.level + 1 if parent else 0
        self.cost = self.calc_cost()

    def calc_cost(self) -> int:
        n = len(self.state)
        count = 0
        for i in range(n):
            for j in range(n):
                count += int(self.state[i][j] and self.state[i][j] != self.final[i][j])
        return count

    def new_node(self, move: Pos) -> Node:
        state = copy.deepcopy(self.state)  # new state
        pos = self.pos + move  # new pos

        if not pos.is_safe(len(state)):
            return False

        state[pos.i][pos.j], state[self.pos.i][self.pos.j] = (
            state[self.pos.i][self.pos.j],
            state[pos.i][pos.j],
        )

        return Node(parent=self, state=state, final=self.final, pos=pos)

    def print_state(self) -> None:
        for row in self.state:
            print(" ".join(map(str, row)))

    def __lt__(self, other: Node):
        return self.cost < other.cost


def printPath(root: Node):
    if root is None:
        return

    printPath(root.parent)
    root.print_state()
    print()


def solve_8_puzzle(
    initial: list[list[int]], final: list[list[int]], pos_z: Pos
) -> list[str]:
    """
    Function to solve the 8-Puzzle Problem using search algorithms like A* or BFS.

    The 8-Puzzle problem consists of a 3x3 grid with 8 numbered tiles and one empty space. The goal is to move the tiles
    to match the goal state by sliding them into the empty space. The problem can be solved optimally using A* search
    with a heuristic (e.g., Manhattan distance), or sub-optimally using BFS or DFS.

    Args:
    start_state (list[list[int]]): The initial configuration of the 8-puzzle, represented as a 3x3 list of integers
                                   where 0 represents the empty space.
    goal_state (list[list[int]]): The target configuration of the 8-puzzle.

    Returns:
    list[str]: A list of moves ("up", "down", "left", "right") representing the steps to reach the goal state.

    Time Complexity:
    - O(b^d) where `b` is the branching factor (up to 4 moves), and `d` is the depth of the solution.

    Space Complexity:
    - O(b^d) for storing the explored states and the priority queue.

    Example:
    >>> start_state = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
    >>> goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    >>> solve_8_puzzle(start_state, goal_state)
    ['right', 'down', 'left']  # Example solution steps
    """

    root = Node(parent=None, state=initial, final=final, pos=pos_z)
    actions = [root]
    possible_moves = [Pos(1, 0), Pos(0, -1), Pos(-1, 0), Pos(0, 1)]
    # hq.heappush(actions, )
    while actions:
        node_min = hq.heappop(actions)
        if node_min.cost == 0:
            return printPath(node_min)

        for move in possible_moves:
            if new_child := node_min.new_node(move):
                hq.heappush(actions, new_child)


initial = [[1, 2, 3], [5, 6, 0], [7, 8, 4]]
final = [[1, 2, 3], [5, 8, 6], [0, 7, 4]]

solve_8_puzzle(
    initial=initial,
    final=final,
    pos_z=Pos(1, 2),
)
