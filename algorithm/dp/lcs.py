def pretty_print(mat):
    for row in mat:
        for col in row:
            print("{: >3}".format(col), end=" ")
        print()


def longest_common_subsequence(
    X: str,
    Y: str,
    i: int,
    j: int,
    memo: list[list[int]],
) -> int:
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
    longest_common_subsequence.call_count += 1
    if i < 0 or j < 0:
        return 0

    # COMMENT TO COMPARE
    if memo[i][j] != -1:
        return memo[i][j]

    if X[i] == Y[j]:
        memo[i][j] = 1 + longest_common_subsequence(X, Y, i - 1, j - 1, memo)
        return memo[i][j]

    memo[i - 1][j] = longest_common_subsequence(X, Y, i - 1, j, memo)
    memo[i][j - 1] = longest_common_subsequence(X, Y, i, j - 1, memo)

    return max(
        memo[i - 1][j],
        memo[i][j - 1],
    )


X = "ABCBDAB"
Y = "BDCAB"
memo = [[-1 for j in Y] for i in X]
longest_common_subsequence.call_count = 0
print(
    f"LCS:={longest_common_subsequence(
        X,
        Y,
        len(X) - 1,
        len(Y) - 1,
        memo,
    )}"
)

pretty_print(memo)
print(f"called:={longest_common_subsequence.call_count}")