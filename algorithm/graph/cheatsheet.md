## BFS

1. Initialize a queue and add the starting node to it.
2. Mark the starting node as visited.
3. While the queue is not empty, dequeue a node, process it, and enqueue all its unvisited neighbors.
4. Repeat until all reachable nodes are visited.

## DFS

1. Initialize a stack (or use recursion for recursive DFS) and add the starting node to it.
2. Mark the starting node as visited.
3. While the stack is not empty, pop a node, process it, and push all its unvisited neighbors onto the stack.
4. Continue until all reachable nodes are visited.

## Detect Cycle

1. For each node, if it hasn't been visited, perform a DFS or recursive DFS.
2. For an undirected graph, check if any visited neighbor is not the parent.
3. For a directed graph, track the recursion stack. If a node in the current path is revisited, there is a cycle.
4. If a cycle is detected during the traversal, return True. If no cycles are found, return False.


## Dijkstra
    
1. Initialize a distance array with infinity (`float('inf')`) for all vertices except the starting vertex, which is set to 0.
2. Use a priority queue (min-heap) to select the vertex with the smallest known distance that hasn't been processed yet.
3. For the selected vertex, update the distances to its adjacent vertices if a shorter path is found.
4. Continue this process until all vertices are processed or the priority queue is empty.
5. Return the distance array, which will contain the shortest distances from the start vertex to all other vertices.