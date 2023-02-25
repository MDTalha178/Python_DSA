""""
In this we solve a problem sum of given problem
"""

# Problem Statement:
"""
Given an array of length N, you need to find and print the sum of all elements of the array.
Input Format :
Line 1 : An Integer N i.e. size of array
Line 2 : N integers which are elements of the array, separated by spaces
Sample Input :
3
9 8 9
Sample Output :
26
"""
# Solution:

# size of Array
size_of_array = int(input())
# creating an Array
array = [int(i) for i in input().split(' ')]

"""
step-1:we initialize a variable which store a sum of array
Step-2: Iterate an Array sum of an every element
Step-3: print a sum after ending a loop
"""
sum_of_array = 0
# using a for loop to iterate on every element
for i in array:
    # sum every element of array with sum_of_array which we initialize at starting
    sum_of_array += i  # this line same as: sum_of_array = sum_of_array + i
# printing our final sum of Array
print("Sum of Array {}".format(sum_of_array))
