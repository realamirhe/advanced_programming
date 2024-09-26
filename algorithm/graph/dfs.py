def dfs(graph: dict[int, list[int]], start: int) -> list[int]:
    """
    Function to perform Depth-First Search (DFS) on a graph starting from a given node.

    Depth-First Search (DFS) is an algorithm for traversing or searching tree or graph data structures.
    It explores as far as possible along each branch before backtracking, effectively following a "deep" path
    before exploring neighbors.

    Args:
    graph (dict[int, list[int]]): A dictionary representing the adjacency list of the graph.
                                  The keys are node identifiers, and the values are lists of neighboring nodes.
    start (int): The starting node for the DFS traversal.

    Returns:
    list[int]: A list of nodes in the order they are visited during DFS.

    Time Complexity:
    - O(V + E), where V is the number of vertices (nodes) and E is the number of edges.

    Space Complexity:
    - O(V) for the stack (or recursion depth) and visited set.

    Example:
    >>> graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    >>> dfs(graph, 0)
    [0, 2, 3, 1]  # DFS traversal order
    """
    ...
