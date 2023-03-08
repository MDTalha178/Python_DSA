"""
Tn this we need to check array rotation
"""
# Problem statement
"""
Check Array Rotation
You have been given an integer array/list(ARR) of size N. It has been sorted(in increasing order) and then rotated by 
some number 'K' (K is greater than 0) in the right hand direction.
Sample Input 1:
1
6
5 6 1 2 3 4
Sample Output 1:
2
"""
# Solution1.1
# size of array
size_of_array = int(input())
# taking input of array
array = [int(i) for i in input().split()]

# rotate index
rotate_index = 0

for i in range(size_of_array):
    if array[i] > array[i+1]:
        rotate_index = i+1
        break

print(rotate_index)
