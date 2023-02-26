"""
In this we need to find pair sum problem
"""
# Problem Statement:
"""
Pair Sum
Send Feedback
You have been given an integer array/list(ARR) and a number X. 
Find and return the total number of pairs in the array/list which sum to X.
Sample Input 1:
1
9
1 3 6 2 5 4 3 2 4
7
Sample Output 1:
7
"""
# Solution:
# Size of Array
size_of_array = int(input())
# creating an Array
array = [int(i) for i in input().split(' ')]
sum_number = int(input())
# storing a pair some count
sum_count = 0
for i in range(size_of_array):
    for j in range(i + 1, size_of_array):
        if array[i] + array[j] == sum_number:
            sum_count += 1

print(sum_count)
