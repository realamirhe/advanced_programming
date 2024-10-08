def combine(A: list[int], B: list[int]):
    i = 0
    j = 0
    combined_array = []
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            combined_array.append(A[i])
            i += 1
        else:
            combined_array.append(B[j])
            j += 1

    while i < len(A):
        combined_array.append(A[i])
        i += 1

    while j < len(B):
        combined_array.append(B[j])
        j += 1

    print(f"COM({combined_array})")
    return combined_array


def merge_sort(arr: list[int]) -> list[int]:
    """
    Function to perform Merge Sort on a given list of integers.

    Merge Sort is a divide-and-conquer algorithm that recursively splits the input list into two halves,
    sorts each half, and then merges the two sorted halves to produce the final sorted list.

    Args:
    arr (list[int]): The input list of integers to be sorted.

    Returns:
    list[int]: A new list containing the sorted elements from the input list.

    Time Complexity:
    - O(n log n), where `n` is the number of elements in the list.

    Space Complexity:
    - O(n) for the additional space needed to merge the sorted halves.

    Example:
    >>> arr = [38, 27, 43, 3, 9, 82, 10]
    >>> merge_sort(arr)
    [3, 9, 10, 27, 38, 43, 82]  # Sorted list
    """
    print(f"MS({arr})")
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return combine(left, right)


arr = [1, 7, 2, 3, 9, 0, -1, 4]
print(merge_sort(arr))