def bfs(graph: dict[int, list[int]], start: int) -> list[int]:
    """
    Function to perform Breadth-First Search (BFS) on a graph starting from a given node.

    Breadth-First Search (BFS) is an algorithm for traversing or searching tree or graph data structures.
    It explores the neighbor nodes at the present depth prior to moving on to nodes at the next depth level.

    Args:
    graph (dict[int, list[int]]): A dictionary representing the adjacency list of the graph.
                                  The keys are node identifiers, and the values are lists of neighboring nodes.
    start (int): The starting node for the BFS traversal.

    Returns:
    list[int]: A list of nodes in the order they are visited during BFS.

    Time Complexity:
    - O(V + E), where V is the number of vertices (nodes) and E is the number of edges.

    Space Complexity:
    - O(V) for the queue and visited set.

    Example:
    >>> graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    >>> bfs(graph, 0)
    [0, 1, 2, 3]  # BFS traversal order
    """
    ...
