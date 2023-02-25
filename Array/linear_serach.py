"""
In this we write an Algorithm for Linear search
"""
# Linear Search:
"""
Linear Search is a algorithm in which we find a given number is present in the array at which index
Example:
array = [1,2 3, 4]
# Number which we need to find at which index: 4
output:3
Because 4 its present at 3rd index
"""

# size of Array
size_of_array = int(input())

# Number which needs to be find
number_find = int(input())

# creating an Array
array = [int(i) for i in input().split(' ')]

# Solution: without using function
"""
Step-1: We iterate on an array of every element
Step-2:we compare every element with a given number 
Step-3: if we found that element we will return index number or we  not found we return -1
"""
index_number = 0
# iterating on an array
for i in range(size_of_array):
    if array[i] == number_find:
        index_number = i
# printing a final result
print("index number {} without function solution".format(index_number))


# Solution: with using function
def linear_search(array_with_func_para: list, find_number_with_func: int, size_of_array_with_func_para: int):
    """
    this function basically run on linear serach
    :param array_with_func_para: array
    :param find_number_with_func: number which needs to be find in the array
    :param size_of_array_with_func_para: size of array
    :return: index number if we found is not, so we will return -1
    """
    for i in range(size_of_array_with_func_para):
        # comparing every element with find number
        if array_with_func_para[i] == find_number_with_func:
            # if condition will True, or  we found return that index number
            return i  # i means index
    # if not found that number in this array we will return -1
    return -1


# calling function
index_number = linear_search(array, number_find, size_of_array)
print("index number {} using function solution".format(index_number))
