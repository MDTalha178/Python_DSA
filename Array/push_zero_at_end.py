"""
In this push every zero at the end of given array
"""
# Problem statement:
"""
Push Zeros to end
Send Feedback
You have been given a random integer array/list(ARR) of size N. You have been required to push all the zeros that are present in the array/list to the end of it. Also, 
make sure to maintain the relative order of the non-zero elements.
Sample Input 1:
1
7
2 0 0 1 3 0 0
Sample Output 1:
2 1 3 0 0 0 0
"""
# Solution
# size of array
size_of_array = int(input())
# taking input of array
array = [int(i) for i in input().split()]
# non zero
non_zero = 0
for i in range(size_of_array):
    if array[i] != 0:
        temp = array[i]
        array[i] = array[non_zero]
        array[non_zero] = temp
        non_zero += 1

print(array)