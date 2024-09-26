def solve_8_puzzle(
    start_state: list[list[int]], goal_state: list[list[int]]
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
    ...
