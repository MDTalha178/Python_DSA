"""
In this we swap alternate element
"""
# Problem Statement:
"""
You have been given an array/list(ARR) of size N. You need to swap every pair of alternate elements in the array/list.
You don't need to print or return anything, just change in the input array itself.
Sample Input 1:
1
6
9 3 6 12 4 32
Sample Output 1 :
3 9 12 6 32 4
"""
# Solution:
"""
Step-1: we will iterate over the array
Setup -2: we will swap every element with each other
Note:
After swapping interment in a for loop will be 2
"""
# size of Array
size_of_array = int(input())

# creating an Array
array = [int(i) for i in input().split(' ')]
# using a for loop
for i in range(0, (len(array)-1), 2):
    # swap every element
    array[i], array[i + 1] = array[i + 1], array[i]
print(array, "After swapping")
