""""
In this we need to print a given 2d array in a spiral form
"""
# Problem Statement
"""
For a given two-dimensional integer array/list of size (N x M), print it in a spiral form. That is, you need to print in the order followed for every iteration:
a. First row(left to right)
b. Last column(top to bottom)
c. Last row(right to left)
d. First column(bottom to top)

Sample Input 1:
1
4 4 
1 2 3 4 
5 6 7 8 
9 10 11 12 
13 14 15 16
Sample Output 1:
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10 
"""
# taking input number of rows and column
number_of_rows_column = input().split()
# number of rows
number_of_rows = int(number_of_rows_column[0])
#  number of column
number_of_column = int(number_of_rows_column[1])

# array
array = [[int(j) for j in input().split()] for i in range(number_of_rows)]

def spiral_print(arr1:list):
    """
    in this we print a given array in spiral form
    :param arr1:
    :return:
    """
    check_num_rows_even = number_of_rows
    if number_of_rows % 2 != 0:
        check_num_rows_even += 1
    for i in range(check_num_rows_even // 2):
        for j in range(i, number_of_column-i):
            print(arr1[i][j], end=" ")
        for k in range(i+1, number_of_rows-i):
            print(arr1[k][j], end=" ")
        for l in range(number_of_column-2-i, -1+i, -1):
            print(arr1[k][l], end=" ")
        for m in range(number_of_rows-2-i, i, -1):
            print(arr1[m][l], end=" ")

spiral_print(array)