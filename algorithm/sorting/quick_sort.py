import random


def quick_sort(array):
    """
    note: The logic is simple, we start from the leftmost element and keep track of the index of smaller
    (or equal) elements as i . While traversing, if we find a smaller element, we swap the current
    element with arr[i]. Otherwise, we ignore the current element.

    note: https://www.geog.cam.ac.uk/images/research/projects/softwareforthefuture/haskell.png
    todo: select the stability of sorting algorithm?
    """

    if len(array) <= 1:
        return array

    pivot = random.choice(array)
    equal = [i for i in array if i == pivot]
    smaller = [i for i in array if i < pivot]
    larger = [i for i in array if i > pivot]

    return quick_sort(smaller) + equal + quick_sort(larger)


ran_array = [random.randint(0, 10) for i in range(10)]
print(ran_array)
print(quick_sort(ran_array))
