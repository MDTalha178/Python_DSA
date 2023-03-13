"""
In this we need to find row wise sum of a give 2d array
"""
# Problem statement
"""
Row Wise Sum
Send Feedback
For a given two-dimensional integer array/list of size (N x M), find and print the sum of each of the row elements in a 
single line, separated by a single space.

Sample Input 1:
1
4 2 
1 2 
3 4 
5 6 
7 8
Sample Output 1:
3 7 11 15 
"""
# how many rows and column
number_of_rows_column = input().split()
# number of rows
number_of_rows = int(number_of_rows_column[0])
# number of column
number_of_column = int(number_of_rows_column[1])

array = [[int(j) for j in input().split()] for i in range(number_of_rows)]


def row_wise_sum(arr1: list, number_of_rows1: int, number_of_column1):
    """
    we need to print sum of rows
    :param arr1: array
    :param number_of_rows1:int
    :param number_of_column1
    :return: none
    """
    for i in range(number_of_rows):
        sum_rows = 0
        for j in range(number_of_column1):
            sum_rows += arr1[i][j]
        print(sum_rows)


# calling method
row_wise_sum(array, number_of_rows, number_of_column)
