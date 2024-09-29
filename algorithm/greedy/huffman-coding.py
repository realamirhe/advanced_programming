import heapq
from collections import Counter


class Node:
    def __init__(self, character, freq) -> None:
        self.character = character
        self.freq = freq
        self.code = ""
        self.right = None
        self.left = None

    def __lt__(self, next):
        return self.freq < next.freq

    def __repr__(self) -> str:
        return f"({self.character}, {self.freq}, {self.code})"


def get_node_codes(node, occurrences=None):
    if occurrences is None:
        occurrences = {}
    if not node.left and not node.right:
        occurrences[node.character] = node.code
        return

    node.right.code = node.code + "1"
    get_node_codes(node.right, occurrences)

    node.left.code = node.code + "0"
    get_node_codes(node.left, occurrences)

    return occurrences


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
    counter = Counter(data)
    heap = []
    for char, freq in counter.items():
        heapq.heappush(heap, Node(char, freq))

    while len(heap) != 1:
        min_1 = heapq.heappop(heap)
        min_2 = heapq.heappop(heap)
        new_node = Node(
            f"internal_node({min_1.character}, {min_2.character})",
            min_1.freq + min_2.freq,
        )
        new_node.right = min_1
        new_node.left = min_2
        heapq.heappush(heap, new_node)

    return heap.pop()


root = huffman_encoding("manya")
codes = get_node_codes(root)
print(codes)