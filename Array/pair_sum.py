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
# Solution 1.1:
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


# Solution 1.2
def get_pair_sum_count(arr1: list, size_of_arr1: int, sum_num: int):
    """
    count a pair sum
    :param arr1: arr1
    :param size_of_arr1: size of array
    :param sum_num:sum number
    :return: return pair count
    """
    unordered_map = {}
    count = 0
    for i in range(size_of_array):
        if sum_num - arr1[i] in unordered_map:
            count += unordered_map[sum_num - arr1[i]]
        if arr1[i] in unordered_map:
            unordered_map[arr1[i]] += 1
        else:
            unordered_map[arr1[i]] = 1
    return count


print(get_pair_sum_count(array, size_of_array, sum_number))
