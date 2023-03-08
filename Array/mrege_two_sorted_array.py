"""
In this we will two sorted array
"""
# Problem Statement:
"""
You have been given two sorted arrays/lists(ARR1 and ARR2) of size N and M respectively, 
merge them into a third array/list such that the third array is also sorted.
Sample Input 1 :
1
5
1 3 4 7 11
4
2 4 6 13
Sample Output 1 :
1 2 3 4 4 6 7 11 13 
"""
# size of array1
size_of_array1 = int(input())
# taking input of array1
array1 = [int(i) for i in input().split()]

# size of array2
size_of_array2 = int(input())
# taking input of array1
array2 = [int(i) for i in input().split()]

result_array = []
# for first array
start_index1 = 0
end_index1 = size_of_array1-1

# for second array
start_index2 = 0
end_index2 = size_of_array2-1
result_index = 0

while start_index1 < size_of_array1 and start_index2 < size_of_array2:
    if array1[start_index1] < array2[start_index2]:
        result_array.append(array1[start_index1])
        start_index1 += 1
    else:
        result_array.append(array2[start_index1])
        start_index2 += 1

while start_index2 < size_of_array2:
    result_array.append(array2[start_index2])
    start_index2 += 1

while start_index1 < size_of_array1:
    result_array.append(array1[start_index1])
    start_index1 += 1

print(result_array)

