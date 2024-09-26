## Longest Common Subsequence

1. Initialize a 2D table (list) of size (len(X)+1) x (len(Y)+1) to store LCS lengths for each substring pair.
2. Iterate through both strings. If characters match, take the diagonal value from the table and increment it.
3. If characters do not match, take the maximum value from either the top or left cell.
4. The bottom-right cell of the table will contain the length of the LCS.

## Discrete knapsack / (knapsack 01)

1. Initialize a 2D table (list) where each entry `dp[i][j]` represents the maximum value that can be
   obtained with the first `i` items and a knapsack capacity `j`.
2. For each item, check if its weight is less than or equal to the current capacity.
   - If it is, compute the maximum value by either including or excluding the item.
   - Otherwise, exclude the item.
3. The last cell of the table will contain the maximum value for the given capacity.

## Matrix Chain Multiplication

1. Initialize a 2D table (list) `dp` where `dp[i][j]` stores the minimum number of scalar multiplications needed to multiply the matrices from index `i` to `j`.
2. Use a nested loop to fill the table based on increasing chain lengths.
3. For each pair of matrices, compute the cost of multiplying the current chain and split it at every possible position.
4. Return the value in `dp[1][n-1]` (where n is the number of matrices) as the minimum cost.
