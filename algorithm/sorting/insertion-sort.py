import random


def insertion_sort(array):
    """
    note: Insertion sort is a simple sorting algorithm that works by iteratively inserting each element of an unsorted
          list into its correct position in a sorted portion of the list meaning that
          elements with equal values maintain their relative order in the sorted output.
    note: https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif
    todo: select the stability of sorting algorithm?
    """

    for i in range(1, len(array)):
        key = array[i]
        for j in range(i - 1, -1, -1):
            if array[j] > key:
                array[j + 1] = array[j]
                array[j] = key
            else:
                break
    return array


def insertion_sort_complicated_version(array):
    for i in range(1, len(array)):
        key = array[i]
        for j in range(i - 1, -1, -1):
            if array[j] > key:
                array[j + 1] = array[j]
                if j == 0:
                    array[j] = key
            else:
                array[j + 1] = key
                break
    return array


ran_array = [random.randint(0, 10) for i in range(10)]
print(ran_array)
print(insertion_sort(ran_array))
