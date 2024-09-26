def longest_common_subsequence(X: str, Y: str) -> int:
    """
    Function to compute the length of the Longest Common Subsequence (LCS) between two strings.

    The Longest Common Subsequence (LCS) is the longest sequence that can be found in both strings
    such that the order of characters is preserved, but not necessarily contiguous.

    Args:
    X (str): The first string.
    Y (str): The second string.

    Returns:
    int: The length of the longest common subsequence between the two strings.

    Time Complexity:
    - O(m * n), where m and n are the lengths of the input strings X and Y.

    Space Complexity:
    - O(m * n) for the 2D table to store intermediate results.

    Example:
    >>> X = "ABCBDAB"
    >>> Y = "BDCAB"
    >>> longest_common_subsequence(X, Y)
    4  # LCS length is 4 ("BCAB" is the LCS)
    Companies: Amazon, Microsoft, Citrix
    """
    ...
