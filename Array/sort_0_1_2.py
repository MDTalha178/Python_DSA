"""
in this we will sort a given array 0 1 2
"""
# Problem Statement:
"""
Sort 0 1 2
Send Feedback
You are given an integer array/list(ARR) of size N. It contains only 0s, 1s and 2s. 
Write a solution to sort this array/list in a 'single scan'.
'Single Scan' refers to iterating over the array/list just once or to put it in 
other words, you will be visiting each element in the array/list just once.
Sample Input 1:
1
7
0 1 2 0 2 0 1
Sample Output 1:
0 0 0 1 1 2 2 
"""
# size of array
size_of_array = int(input())
# taking input of array
array = [int(i) for i in input().split()]

# start_index
start_index = 0
# mid_index
mid_index = 0
# end_index
end_index = size_of_array - 1

while mid_index <= end_index:
    if array[mid_index] == 0:
        array[start_index], array[mid_index] = array[mid_index], array[start_index]
        start_index += 1
        mid_index += 1
    elif array[mid_index] == 1:
        mid_index += 1
    else:
        array[mid_index], array[end_index] = array[end_index], array[mid_index]
        end_index -= 1

print(array)
