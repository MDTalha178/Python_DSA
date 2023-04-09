"""
In this we need to print a given 2d array in wave form
"""
# Problem Statement
"""
Wave Print
Send Feedback
For a given two-dimensional integer array/list of size (N x M), print the array/list in a sine wave order, i.e, print the 
first column top to bottom, next column bottom to top and so on.
Sample Input 1:
1
3 4 
1  2  3  4 
5  6  7  8 
9 10 11 12
Sample Output 1:
1 5 9 10 6 2 3 7 11 12 8 4
"""
# solution
# taking number of rows and column
number_of_rows_column = input().split()
# number of rows
number_of_rows = int(number_of_rows_column[0])
# number of column
number_of_column = int(number_of_rows_column[1])

array = [[int(j) for j in input().split()] for i in range(number_of_rows)]


# function for printing
def wave_print(arr1:list):
    """
    we need to print 2d arrays in wave form
    :param arr1:
    :return:
    """
    for i in range(number_of_column):
        for j in range(number_of_rows):
            if i % 2 == 0:
                print(arr1[j][i], end=" ")
            else:
                print(arr1[number_of_rows-j-1][i], end=" ")


# calling method
wave_print(array)



