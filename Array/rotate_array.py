"""
In this we will rotate a given array
"""
# Problem Statement
"""
Rotate array
Send Feedback
You have been given a random integer array/list(ARR) of size N. Write a function that rotates 
the given array/list by D elements(towards the left).
Sample Input 1:
1
7
1 2 3 4 5 6 7
2
Sample Output 1:
3 4 5 6 7 1 2
"""
# Solution1.1
# size of array
size_of_array = int(input())
# taking input of array
array = [int(i) for i in input().split()]

# rotate index
rotate_index1 = int(input())


def rotate_array(arr1: list, size_of_arr1: int, rotate_index: int):
    """
    rotate an given array
    :param arr1:
    :param size_of_arr1:
    :param rotate_index: rotate_index
    :return: array
    """
    temp_array = []
    for i in range(rotate_index, size_of_arr1):
        temp_array.append(arr1[i])
    for i in range(0, rotate_index):
        temp_array.append(i)
    for i in range(size_of_array):
        array[i] = temp_array[i]


rotate_array(array, size_of_array, rotate_index1)
print(array)
