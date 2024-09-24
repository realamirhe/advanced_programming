def bubble_sort(array):
    """
    note: traverse from left and compare adjacent elements and the higher one is placed at right side.
    In this way, the largest element is moved to the rightmost end at first.
    This process is then continued to find the second largest and place it and so on until the data is sorted.
    note: https://en.wikipedia.org/wiki/File:Bubble-sort-example-300px.gif
    todo: optimize with the flag
    todo: select the stability of sorting algorithm?
    note: this is in-place sorting algorithm
    """
    count = 0
    for i in range(0, len(array)):
        swapped = False
        for j in range(0, len(array) - i - 1):
            count += 1
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            print(count)
            return array
    print(count)
    return array


# ran_array = [random.randint(0, 10) for i in range(10)]
ran_array = [1, 1, 2, 2, 2, 3, 4, 9, 10, 10]
print(ran_array)
print(bubble_sort(ran_array))
