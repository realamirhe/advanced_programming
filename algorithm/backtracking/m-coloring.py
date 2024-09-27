def m_coloring(graph: list[list[int]], m: int) -> bool:
    """
    Function to solve the M-Coloring problem using backtracking.

    The M-Coloring problem involves coloring the vertices of a graph with at most `m` colors such that no two adjacent
    vertices share the same color. The backtracking approach tries to assign colors to each vertex and backtracks if
    a conflict (adjacent vertices with the same color) is detected.

    Args:
    graph (list[list[int]]): A 2D adjacency matrix representing the graph, where `graph[i][j] == 1` means
                             there is an edge between vertex `i` and vertex `j`, and `graph[i][j] == 0` means no edge.
    m (int): The maximum number of colors available for coloring the graph.

    Returns:
    bool: True if the graph can be colored with at most `m` colors, otherwise False. The graph is modified in-place
          to represent the coloring solution (if any).

    Time Complexity:
    - O(m^n), where `n` is the number of vertices in the graph, since each vertex has `m` possible colors.

    Space Complexity:
    - O(n) for storing the color assignments.

    Example:
    >>> graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
    ]
    >>> m = 3
    >>> m_coloring(graph, m)
    True  # The graph can be colored using 3 colors
    """
    ...
