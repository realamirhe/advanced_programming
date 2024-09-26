## BFS

1. Initialize a queue and add the starting node to it.
2. Mark the starting node as visited.
3. While the queue is not empty, dequeue a node, process it, and enqueue all its unvisited neighbors.
4. Repeat until all reachable nodes are visited.

## Detect Cycle

1. For each node, if it hasn't been visited, perform a DFS or recursive DFS.
2. For an undirected graph, check if any visited neighbor is not the parent.
3. For a directed graph, track the recursion stack. If a node in the current path is revisited, there is a cycle.
4. If a cycle is detected during the traversal, return True. If no cycles are found, return False.

## DFS

1. Initialize a stack (or use recursion for recursive DFS) and add the starting node to it.
2. Mark the starting node as visited.
3. While the stack is not empty, pop a node, process it, and push all its unvisited neighbors onto the stack.
4. Continue until all reachable nodes are visited.
