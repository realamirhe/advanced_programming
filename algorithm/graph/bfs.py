def bfs_util(graph, visited, parent):
    queue = []
    queue.append(parent)
    while queue:
        parent_for_the_end_of_the_class = queue.pop(0)  # todo: rename please
        if visited[parent_for_the_end_of_the_class]:
            continue
        print(f"N({parent_for_the_end_of_the_class}) ✅")
        visited[parent_for_the_end_of_the_class] = True
        for child in graph[parent_for_the_end_of_the_class]:
            queue.append(child)


def bfs(graph: dict[int, list[int]]) -> list[int]:
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
    visited = {key: False for key in graph.keys()}
    for child in graph.keys():
        bfs_util(graph, visited, child)


graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2], 7: [8, 9], 9: [8], 8: []}
bfs(graph)