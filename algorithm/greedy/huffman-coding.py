def huffman_encoding(data: str) -> tuple[dict, str]:
    """
    Function to perform Huffman encoding on a given input string.

    Huffman coding is a lossless data compression algorithm. The algorithm works by assigning variable-length codes
    to input characters, with shorter codes assigned to more frequent characters. This results in efficient compression
    by reducing the overall number of bits used.

    Args:
    data (str): The input string to be encoded.

    Returns:
    tuple[dict, str]:
        - dict: A dictionary where the keys are characters and values are their corresponding Huffman codes.
        - str: The encoded string (i.e., the input string represented as a series of 0s and 1s based on the Huffman tree).

    Time Complexity:
    - The time complexity for building the Huffman tree is O(n log n), where `n` is the number of unique characters.

    Space Complexity:
    - O(n) for storing the frequency table, the Huffman tree, and the codes dictionary.

    Example:
    >>> huffman_encoding("hello world")
    ({'h': '101', 'e': '011', 'l': '00', 'o': '10', 'w': '1101', 'r': '1100', 'd': '111'}, '101011000010110011001110111')

    HINT: https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/
    Companies: Amazon, Microsoft, Samsung
    """
    ...
