"""
In this we find a duplicate an element in a given Array
"""
# Problem Statement:
"""
Find Duplicate
Send Feedback
You have been given an integer array/list(ARR) of size 
N which contains numbers from 0 to (N - 2). Each number is present at least once. 
That is, if N = 5, the array/list constitutes values ranging from 0 to 3 and among these, 
there is a single integer value that is present twice. You need to find and return that 
duplicate number present in the array.
Sample Input 1:
1
9
0 7 2 5 4 7 1 3 6
Sample Output 1:
7
"""
# Solution 1.1:
# Size of Array
size_of_array = int(input())
# creating an Array
array = [int(i) for i in input().split(' ')]
"""
Step 1: we declare an empty dictionary in which store an occurrence og every element
Step 2: we find that element from a dictionary  whose count is 1 means occurrence 1
"""
#
occurrence_count = dict()
for i in array:
    # if we will get that element in dictionary we will increment a count with 1
    occurrence_count[i] = occurrence_count.get(i, 0) + 1
duplicate_element = 0
for i in occurrence_count.keys():
    if occurrence_count[i] > 1:
        duplicate_element = i
print("Duplicate element in a array is {}".format(duplicate_element))

# Solution 1.2:
for i in range(0, size_of_array):
    # comparing every element with each other if they are equal means they are dupliacte
    for j in range(0, size_of_array):
        if array[i] == array[j]:
            duplicate_element = array[i]
print("Duplicate element in a array {}".format(duplicate_element))
