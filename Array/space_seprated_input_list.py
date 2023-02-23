"""we will take space separated input from the user
"""
# take an input line separated for a list
"""how to take line separated input from the user for list
"""
# In this  we store all user element
result = []
# how numbers we want to take input from the user
number_of_elements = int(input())
# running a for a loop for number_of_elements time
for i in range(number_of_elements):
    # taking an input from user
    take_input = int(input())
    # inserting an element in a result list
    result.append(take_input)
print(result, "from line separated input")

# take an input Space separated for a list
"""
how to take a input for space separated list
"""
# how numbers we want to take input from the user
number_of_elements = input()
space_separated_list = []
# split() method will split your sting with a given condition into list
"""
so here we split out user input sting number and condition will be space
if you want to know more about split() follow the given
https://www.w3schools.com/python/ref_string_split.asp
"""
split_list = number_of_elements.split(' ')
for i in split_list:
    # insert all the element in space_separated_list but inserting we need to convert into integer
    space_separated_list.append(int(i))
print(space_separated_list, "from space separated list")

# if you want to do in one line
"""
Here ww used list compression if you want know more follow the given link
https://www.w3schools.com/python/python_lists_comprehension.asp
"""
space_separated_list = [int(i) for i in input().split()]
print(space_separated_list)
