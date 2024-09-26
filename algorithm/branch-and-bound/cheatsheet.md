## Knapsack Branch and Bound

1. Use a priority queue (or heap) to explore the search space based on nodes representing partial solutions.
2. Each node represents a state where certain items are either included or excluded.
3. Calculate the upper bound for each node, which is the best possible value achievable from that node onwards.
4. If the current node cannot lead to a better solution than the best-known solution, prune the node.
5. Continue branching until all promising nodes are explored.

## Job Assignment

1. Use dynamic programming or backtracking to explore all possible assignments of jobs to workers.
2. For the dynamic programming approach, maintain a DP table where each state represents the minimum cost
   for a subset of workers and assigned jobs.
3. Use bit-masking or recursive backtracking to assign jobs, ensuring no job is assigned to more than one worker.
4. At each step, update the cost based on the assignment and return the minimum total cost.

## 8 Puzzle

1. Use A\* search with a priority queue to explore the state space. The priority queue is sorted based on
   the total cost (g + h), where `g` is the cost to reach the current state and `h` is the heuristic cost.
2. The heuristic can be the Manhattan distance between the current state and the goal state.
3. At each step, generate all possible states by sliding a tile into the empty space.
4. Continue exploring the states with the lowest total cost until the goal state is reached.
5. Trace back the steps to form the solution path.

## N Queen

1. Use backtracking to place queens row by row.
2. For each row, check if a queen can be placed in a given column without being attacked.
   Ensure no other queen exists in the same column, or diagonals.
3. If a valid placement is found, proceed to the next row. If no valid column exists, backtrack to the previous row.
4. Once all queens are placed, add the solution to the result list.
5. Continue until all possible placements are explored.
