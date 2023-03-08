"""
In this we find the second-largest element in a given array
"""
# Problem statement
"""
Second Largest in array
Send Feedback
You have been given a random integer array/list(ARR) of size N. You are required to find and return 
the second largest element present in the array/list.
Sample Input 1:
1
7
2 13 4 1 3 6 28
Sample Output 1:
13
"""
# Solution
# size of array
size_of_array = int(input())
# taking input of array
array = [int(i) for i in input().split()]

# first sort array
array.sort()
print(array[-2])
