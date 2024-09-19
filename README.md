# Advanced Programming Lecture

## Algorithm
> **Tip 1:** All content is going to be tough and asked in Python programming language.
> **Tip 2:** We are going to define the computation time complexity using BigO notation, solve some examples, and learn how to estimate the time complexity of algorithms. We will continuously update our understanding throughout the course.

### 1. Sorting Algorithms
- **Introduction to Sorting**
    - Sorting refers to the process of arranging data in a particular order.
- **Bubble Sort**
    - Simple but inefficient sorting algorithm with time complexity O(n²).
- **Insertion Sort**
    - Efficient for small datasets, average time complexity O(n²).
- **Quick Sort**
    - Divide and conquer algorithm with average time complexity O(n log n).
- **Stable and Unstable Sorting Algorithms**
    - Explanation of sorting algorithms that preserve the order of equal elements (stable) and those that don't (unstable).
- **Lower Bound for Comparison-Based Sorting Algorithms**
    - Theoretical limit: O(n log n) is the lower bound for comparison-based sorting algorithms.

### 2. Greedy Algorithms
- **Introduction to Greedy Algorithms**
    - A greedy algorithm makes the locally optimal choice at each step in the hope of finding a global optimum.
- **Huffman Coding**
    - A compression algorithm using a binary tree for efficient data encoding.
- **Knapsack**
    - Maximizing the total value within a weight constraint.
- **Job Sequencing Problem**
    - Maximizing profit by scheduling jobs within deadlines.

### 3. Dynamic Programming Algorithms
- **Introduction to Dynamic Programming**
    - A technique for solving problems by breaking them into overlapping subproblems, storing results to avoid redundant work.
- **Longest Common Subsequence**
    - Finding the longest subsequence common to two sequences.
- **0-1 Knapsack Problem**
    - Maximizing value with weight constraints, where items can either be taken or not.
- **Matrix Chain Multiplication**
    - Parenthesizing a matrix product to minimize computation.

### 4. Backtracking Algorithm
- **Introduction to Backtracking**
    - A general algorithmic approach to solving constraint satisfaction problems incrementally.
- **The Knight’s Tour Problem**
    - Finding a sequence where a knight visits all squares exactly once on a chessboard.
- **N Queen Problem**
    - Placing N queens on an NxN chessboard so no two queens threaten each other.
- **Subset Sum**
    - Determining if a subset of a set has a sum equal to a target value.
- **Sudoku Solver**
    - Solving the popular 9x9 puzzle game using backtracking.
- **m Coloring Problem**
    - Coloring the vertices of a graph such that no adjacent vertices have the same color using m colors.

### 5. Divide and Conquer Algorithm
- **Introduction to Divide and Conquer**
    - A strategy of solving complex problems by breaking them into subproblems.
- **Merge Sort**
    - Time complexity O(n log n), divides arrays and merges sorted subarrays.
- **Binary Search**
    - Efficient search algorithm with time complexity O(log n).

### 6. Graph Algorithms
- **Introduction to Graph Algorithms**
    - Graph algorithms are algorithms that use graph theory for their formulation and problem-solving.
- **BFS and DFS**
    - BFS (Breadth-First Search) and DFS (Depth-First Search) for exploring graph nodes.
- **Cycles in Graph**
    - Detecting cycles in a directed/undirected graph.
- **Shortest Paths**
    - Algorithms for finding the shortest path between nodes (Dijkstra's and Bellman-Ford).

### 7. Branch and Bound Algorithms
- **Introduction to Branch and Bound Algorithms**
    - Optimization algorithms that systematically search for an optimal solution by pruning branches that cannot yield better results.
- **Job Assignment Problem**
    - Assigning jobs to minimize cost.
- **N Queen Problem (Branch and Bound Approach)**
    - Using a more efficient strategy to solve N Queens.
- **8 Puzzle Problem**
    - Solving the sliding tile puzzle by minimizing moves.
- **0/1 Knapsack (Branch and Bound Approach)**
    - Optimizing the solution to the knapsack problem using branch and bound.


## Primitive Types and Pointers
> We are going to teach the course in Python but demonstrate examples using C/C++ for pointers.

- **Primitive Types in Python**
    - Integers, Floats, Strings, and Booleans.
- **Pointers in C/C++**
    - Explanation of memory addresses, pointer arithmetic, and dereferencing.
- **Comparison of Python Variables vs C/C++ Pointers**
    - Highlighting the difference between Python's high-level variable handling and C/C++ pointer manipulation.

## Data Structures
> Implement these data structures in Python, and use them to solve new algorithmic problems.

- **Linked List**
    - A linear data structure consisting of nodes where each node contains data and a reference to the next node.
    - Operations: Insertion, Deletion, Traversal.
- **Stack**
    - Last-In-First-Out (LIFO) structure. Operations include `push`, `pop`, `peek`.
    - Applications: Expression evaluation, backtracking.
- **Queue**
    - First-In-First-Out (FIFO) structure. Operations include `enqueue`, `dequeue`, `peek`.
    - Applications: Scheduling, buffering.
- **Tree (Binary Tree)**
    - A hierarchical data structure with a root node, left, and right subtrees.
    - Operations: Insertion, Deletion, Traversal (In-order, Pre-order, Post-order).
    - Applications: Search operations, expression trees.

## Real-World Topics (AI & Bio-Included)
- **Environment setup**
    - Setting up a virtual environment ensures that your Python project is isolated from global dependencies, preventing conflicts.
    - Example: Creating a data science environment
- **Python Decorators**
    - A design pattern that allows the behavior of functions to be modified.
    - Usage in logging, authentication, etc.
- **Jupyter**
    - An open-source web application that allows you to create and share live code, equations, visualizations, and text.
    - Example: Running Python code interactively, displaying data analysis results, and documenting findings in a single notebook interface.
- **Pandas**
    - Data manipulation library used for handling structured data (DataFrames).
    - Example: Loading, cleaning, and analyzing CSV files.
- **NumPy**
    - Library for numerical computations with support for large multi-dimensional arrays and matrices.
    - Example: Efficient matrix operations, random number generation.
- **Matplotlib**
    - A plotting library used for creating static, interactive, and animated visualizations in Python.
    - Example: Creating line plots, bar charts, histograms, and scatter plots to visualize data and trends.
- **Sklearn (Scikit-learn)**
    - A library for machine learning. Includes simple and efficient tools for data analysis and modeling.
    - Example: Building a classification model using decision trees.
