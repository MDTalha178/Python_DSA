"""
In this we find Intersection of two Array
"""
# Problem Statement:
"""
Intersection of Two Arrays II
You have been given two integer arrays/list(ARR1 and ARR2) of size N and M, respectively. 
You need to print their intersection; An intersection for this problem can be defined when both the 
arrays/lists contain a particular value or to put it in other words, 
when there is a common value that exists in both the arrays/lists.
Sample Input 1 :
2
6
2 6 8 5 4 3
4
2 3 4 7 
2
10 10
1
10
Sample Output 1 :
2 4 3
10
"""
# Solution 1.1:
# size of Array1
size_of_array1 = int(input())
# creating an Array1
array1 = [int(i) for i in input().split()]

# size of Array2
size_of_array2 = int(input())
# creating an Array1
array2 = [int(i) for i in input().split()]

"""
Step 1:We will using nested for loop 
Step 2: pick one element and compare with second array
Note: 
This is Brute force Approach
Time Complexity: O(n^2)
"""


# declaring a function
def intersection_of_array_btf(arr1: list, arr2: list, size_of_arr1: int, size_of_arr2: int):
    """
    we find intersection of a given array
    :param arr1: array1
    :param arr2: array 2
    :param size_of_arr1: size of arr1
    :param size_of_arr2: size of arr2
    :return: none
    """
    # iterating on first array means arr1
    for i in range(size_of_arr1):
        # iterating on first array means arr1
        for j in range(size_of_arr2):
            # comparing every element of array1 with array2
            if arr1[i] == arr2[j]:
                # if condition will True means intersection
                print(arr1[i], end=" ")


# calling function
intersection_of_array_btf(array1, array2, size_of_array1, size_of_array2)
print()


def intersection_of_array(arr1: list, arr2: list, size_of_arr1: int, size_of_arr2: int):
    """
       we find intersection of a given array
       :param arr1: array1
       :param arr2: array 2
       :param size_of_arr1: size of arr1
       :param size_of_arr2: size of arr2
       :return: none
    """
    # we need to sort for better complexity
    arr1.sort()
    arr2.sort()
    # we need to declare a variable which start from zero for arr1
    start_point_arr1 = 0
    # we need to declare a variable which start from zero for arr1
    start_point_arr2 = 0
    # running a while until start_point_arr1 less than size_of_arr1 and start_point_arr2 is less than size_of_arr2
    while start_point_arr1 < size_of_arr1 and start_point_arr2 < size_of_arr2:
        # comparing an element of arr1 with arr2
        if arr1[start_point_arr1] == arr2[start_point_arr2]:
            print(arr1[start_point_arr1], end=" ")
            # increment a value of start_point_arr1 and start_point_arr2 with 1
            start_point_arr1 += 1
            start_point_arr2 += 1
        # checking condition
        elif arr1[start_point_arr1] < arr2[start_point_arr2]:
            start_point_arr1 += 1
        else:
            start_point_arr2 += 1


intersection_of_array(array1, array2, size_of_array1, size_of_array2)
