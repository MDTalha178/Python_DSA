"""
In this we perform bubble sort Array
"""
# Problem Statement:
"""
we need to sort a given array using bubble sort algorithm
"""

# size of array
size_of_array = int(input())
# taking input array
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


def bubble_sort(arr1: list, size_if_arr1: int):
    """
    we will sort an array using bubble sort
    :param arr1: arr1
    :param size_if_arr1: size of array
    :return: sorted array
    """
    for i in range(len(arr1)):
        for j in range(len(arr1) - i):
            if arr1[j] > arr1[j + 1]:
                swap(i, j, arr1)


# calling function
bubble_sort(array, size_of_array)
# printing ar array
for i in array:
    print(i, end=" ")
