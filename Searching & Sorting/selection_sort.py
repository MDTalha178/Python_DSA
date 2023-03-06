"""
In this we perform selection sort Algorithm
"""
# Problem statement:
"""
We need to sort an array using selection sort
"""
# size of array
size_of_array = int(input())
# taking input of array
array = [int(i) for i in input().split()]


def swap(index1: int, index2: int, arr1: list):
    """
    we swap two element to each other
    :param index1: index1
    :param index2: index 2
    :param arr1: arr1
    :return: return arr1
    """
    arr1[index1], arr1[index2] = arr1[index2], arr1[index1]


def selection_sort(arr1: list, size_of_arr1: int):
    """
    we sort an array using selection sort
    :param arr1: arr1
    :param size_of_arr1: size of array
    :return: return sorted array
    """
    for i in range(size_of_arr1):
        for j in range(i + 1, size_of_arr1):
            if arr1[i] > arr1[j]:
                swap(i, j, arr1)
    return arr1


selection_sort(array, size_of_array)
# printing an array
for i in array:
    print(i, end=" ")
