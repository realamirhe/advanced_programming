## fraction knapsack

1.  Sort the items in descending order based on their value-to-weight ratio.
2.  Iteratively take as much of the highest value-to-weight ratio item as possible, or a fraction of it if the remaining capacity is less than the item's weight.
3.  Continue until the knapsack is full or all items have been considered.

## huffman coding

1. Calculate the frequency of each character in the input string. `collection.Counter`  
   > `class node {huff, left, right, freq, character}`
2. Build a priority queue (min-heap) where each node is a character and its frequency. `__lt__`
3. Build the Huffman tree by combining nodes with the lowest frequencies.
4. Traverse the Huffman tree to assign binary codes to each character.

## job sequencing

1. Sort all jobs based on their profit in descending order.  
   > `class node {id, deadline, profit}`
2. For each nodes, place it in the first empty position before its deadline