import heapq as hq


class Node:
    def __init__(self, id: str, distance: int):
        self.id = id
        self.distance = distance

    def __lt__(self, next):
        return self.distance < next.distance


def dijkstra_shortest_path(graph: list[list[tuple[int, int]]], start: str) -> list[int]:
    """
    Function to find the shortest paths from a starting vertex to all other vertices in a weighted graph using Dijkstra's algorithm.

    Dijkstra's algorithm works by iteratively selecting the vertex with the smallest known distance, updating the distances
    to its adjacent vertices, and repeating the process until all vertices have been processed. This algorithm is optimal
    for graphs with non-negative weights.

    Args:
    graph (list[list[tuple[int, int]]]): An adjacency list representing the graph, where `graph[u]` is a list of tuples `(v, w)`
                                         representing an edge from vertex `u` to vertex `v` with weight `w`.
    start (int): The starting vertex from which to calculate the shortest paths.

    Returns:
    list[int]: A list of distances where the `i-th` index represents the shortest distance from the starting vertex to vertex `i`.
               If a vertex is unreachable, its distance will be set to infinity (`float('inf')`).

    Time Complexity:
    - O((V + E) log V), where `V` is the number of vertices and `E` is the number of edges, due to the use of the priority queue.
    - O(V 2 ) if you use spanning tree idea

    Space Complexity:
    - O(V + E) for storing the graph, distance array, and priority queue.

    Example:
    >>> graph = [
    [(1, 4), (2, 1)],    # Edges from vertex 0: (0 -> 1, weight 4), (0 -> 2, weight 1)
    [(2, 2), (3, 1)],    # Edges from vertex 1: (1 -> 2, weight 2), (1 -> 3, weight 1)
    [(3, 5)],            # Edge from vertex 2: (2 -> 3, weight 5)
    []                   # No edges from vertex 3
    ]
    >>> start = 0
    >>> dijkstra_shortest_path(graph, start)
    [0, 3, 1, 4]  # Shortest distances from vertex 0 to all other vertices
    # https://stackoverflow.com/a/71666688/10321531
    """
    shortest_distances = {}
    distance = 0
    nodes = [Node(id=start, distance=distance)]
    while nodes:
        node = hq.heappop(nodes)
        if node.id in shortest_distances:
            continue
        shortest_distances[node.id] = node.distance
        for id, weight in graph[node.id]:
            hq.heappush(nodes, Node(id=id, distance=distance + weight))

    return shortest_distances


graph = {
    "a": [("b", 8), ("c", 3), ("d", 6)],
    "b": [("a", 8), ("e", 5)],
    "c": [("a", 3), ("d", 2)],
    "d": [("a", 6), ("c", 2), ("e", 5), ("g", 3)],
    "e": [("b", 5), ("d", 5), ("f", 5)],
    "f": [("e", 5), ("g", 3), ("h", 6)],
    "g": [("d", 3), ("f", 3), ("h", 4)],
    "h": [("g", 4), ("f", 6)],
}


print(dijkstra_shortest_path(graph, "a"))
