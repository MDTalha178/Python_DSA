"""
In this we explore list comprehension
"""
# Problem statement 1.1:
"""
We have a given list and we need to return a list with square of every element we will use both method
Input:
array = [1,2,3,4]
output:
[1,4,9,16]
"""
# without List comprehension

# taking array input from user
array = [int(i) for i in input().split()]
# we need define a new  empty list which store a square of every of element
suq_array = []
for i in array:
    suq_array.append(i * i)
print(suq_array)

# With  List comprehension
suq_array = [i * i for i in array]
print(suq_array)

# Problem Statement 1.2
"""
We need return a list store only even number in list
Input:
array = [1,2,3,4,5,6]
Output:
[2,4,6]
"""
# without List comprehension

# we need define a new  empty list which store a even number
even_list = []
for i in array:
    # checking if number is completely divisible by 2 means its even
    if i % 2 == 0:
        # if its even insert in an even list
        even_list.append(i)

print(even_list, 'Even list without List comprehension')

# List comprehension
even_list = [i for i in array if i % 2 == 0]
print(even_list, 'Even list with List comprehension')

# Problem Statement1.3:
"""
We need to return a list which store only those element which is divisible by 2 and 3
"""
# without List comprehension
# we need define a new  empty list which store a which is divisible by 2 and 3
two_n_three_list = []
for i in array:
    # checking condition if completely divisible by 2
    if i % 2 == 0:
        # checking condition if completely divisible by 2
        if i % 3 == 0:
            two_n_three_list.append(i)

print(two_n_three_list, 'Element which is divisible by 2 and 3 without List comprehension')

# List comprehension
two_n_three_list = [i for i in array if i % 2 == 0 if i % 3 == 0]
print(two_n_three_list, 'Element which is divisible by 2 and 3 with List comprehension')

# Problem Statement 1.4:
"""
We need to return a list which if element is divisible by 2 square of that number rest we store as it is
Input:
array = [1,2 3, 4]
Output = [1,4,3,16]
"""
# without List comprehension
# we need define a new  empty list which store a which is store result
even_squares_list = []
for i in array:
    # checking condition if it is divisible by 2
    if i % 2 == 0:
        # square of element
        even_squares_list.append(i * i)
    else:
        even_squares_list.append(i)

print(even_squares_list, 'Even square without List comprehension')
# List comprehension
even_squares_list = [i if i % 2 == 0 else i for i in array]
print(even_squares_list, 'Even square with List comprehension')
