"""
In this we perform Binary search Algorithm
"""
# Problem Statement
"""
In Binary search we need to find an element on which index is present the given number if that is present
in array we need to return index if that element other wise we return -1

Input: [1,2,3,4,5]
number_need_find = 4
output: 3
"""
# size of array
size_of_array = int(input())
# take input of array
array = [int(i) for i in input().split()]

# find number
number_find = int(input())


def binary_search(arr1: list, number_find_index: int, size_of_arr1: int):
    """
    we will find an index of that element using binary search algorithm
    :param arr1: arr1
    :param number_find_index: find_number
    :param size_of_arr1: size_of_arr1
    :return: index_number
    """
    start = 0
    end = size_of_arr1 - 1
    while start <= end:
        mid = (start + end) // 2
        if arr1[mid] == number_find_index:
            return mid
        elif arr1[mid] > number_find_index:
            end = mid - 1
        else:
            start = mid + 1
    return -1


# calling function
index_number = binary_search(array, number_find, size_of_array)
print(index_number)
