import random


def combine(arr_x, arr_y):
    i, j, combined_array = 0, 0, []
    while i < len(arr_x) and j < len(arr_y):
        if arr_x[i] <= arr_y[j]:
            combined_array.append(arr_x[i])
            i += 1
        else:
            combined_array.append(arr_y[j])
            j += 1

    combined_array += arr_y[j:]
    combined_array += arr_x[i:]
    return combined_array


def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = (len(array)) // 2
    return combine(
        merge_sort(array[:mid]),
        merge_sort(array[mid:]),
    )


ran_array = [random.randint(0, 10) for i in range(10)]
print(ran_array)
print(merge_sort(ran_array))
