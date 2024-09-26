def detect_cycle(graph: dict[int, list[int]]) -> bool:
    """
    Function to detect if there is a cycle in a given graph.

    Cycle detection in a graph can be done using Depth-First Search (DFS) for both directed and undirected graphs.
    For an undirected graph, a cycle is present if during DFS we revisit a visited node that is not the parent of
    the current node. For a directed graph, we use a visited set and a recursion stack to track nodes in the current path.

    Args:
    graph (dict[int, list[int]]): A dictionary representing the adjacency list of the graph.
                                  The keys are node identifiers, and the values are lists of neighboring nodes.

    Returns:
    bool: True if a cycle is detected, otherwise False.

    Time Complexity:
    - O(V + E), where V is the number of vertices (nodes) and E is the number of edges.

    Space Complexity:
    - O(V) for the visited set and recursion stack.

    Example:
    >>> graph = {0: [1], 1: [2], 2: [0], 3: [4]}
    >>> detect_cycle(graph)
    True  # The graph has a cycle (0 -> 1 -> 2 -> 0)
    """
    ...
