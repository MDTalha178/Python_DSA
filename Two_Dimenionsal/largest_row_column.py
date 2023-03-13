"""
In this we need to find largest summ of rows or column
"""
# Problem Statement
"""
Largest Row or Column
Send Feedback
For a given two-dimensional integer array/list of size (N x M), you need to find out which row or column has the largest 
sum(sum of all the elements in a row/column) amongst all the rows and columns.
Input:
4 4
6 9 8 5 
9 2 4 1 
8 3 9 3 
8 7 8 6 
Output
column 0 31
"""
# Solution
# number rows and column
number_of_rows_column = input().split()
# number_of_rows
number_of_rows = int(number_of_rows_column[0])
# number_of_column
number_of_column = int(number_of_rows_column[1])

# array
array = [[int(j) for j in input().split()] for i in range(number_of_rows)]


def largest_row_column(arr1: list):
    """
    we find which row or column have greater sum
    :param arr1:
    :return: largest sum
    """
    # finding the largest sum for rows
    rows_largest_sum = 0
    largest_row = 0
    for i in range(number_of_rows):
        local_sum = 0
        for j in range(number_of_column):
            local_sum += arr1[i][j]
        if local_sum > rows_largest_sum:
            rows_largest_sum = local_sum
            largest_row = i
    # finding sum of column
    column_largest_sum = 0
    largest_column = 0
    i = 0
    while i < number_of_column:
        j = 0
        local_sum = 0
        while j < number_of_rows:
            local_sum += arr1[j][i]
            j += 1
        if local_sum > column_largest_sum:
            column_largest_sum = local_sum
            largest_column = i
        i += 1
    # check condition which one is greater
    if rows_largest_sum > column_largest_sum:
        return f"row {largest_row}"
    else:
        return f"column {largest_column}"


# calling function
result = largest_row_column(array)
print(result)
