"""
find a unique number in the given array
"""
# Problem Statement
"""
Find Unique
You have been given an integer array/list(ARR) of size N. Where N is equal to [2M + 1].
Now, in the given array/list, 'M' numbers are present twice and one number is present only once.
You need to find and return that number which is unique in the array/list.
Sample Input 1:
1
7
2 3 1 6 3 6 2
Sample Output 1:
1
"""
# size of Array
size_of_array = int(input())

# creating an Array
array = [int(i) for i in input().split(' ')]
# initialize dictionary in which store a count of occurrence every number
occurrence_dict = dict()
# using a loop to store occurrence
for i in array:
    occurrence_dict[i] = occurrence_dict.get(i, 0) + 1
#  finding a unique number from occurrence_dict
unique_number = -1
for i in occurrence_dict.keys():
    if occurrence_dict[i] == 1:
        unique_number = i
print(unique_number)