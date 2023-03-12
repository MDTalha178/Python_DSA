"""
In this we learn how take input of 2d list
"""
# Problem Statement 1.1:
"""
How to take input of 2d list
Note:
This jagged list because we not restricting for the number of column
"""
# How many rows and column
number_of_rows_column = input().split()
number_of_rows = int(number_of_rows_column[0])
# number of column
number_of_column = int(number_of_rows_column[1])
# the whole list with number_of_rows and number_of_column
whole_list = input().split()

# taking input of 2d list
array_2d = [[int(whole_list[number_of_rows_column * i + j]) for j in range(
    number_of_column)] for i in range(number_of_rows)
            ]
print(array_2d)
