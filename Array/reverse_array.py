"""
In  this we will reverse an array
"""
# Problem Statement
"""
We need print reverse a  given array
we have multiple approach to solve this problem
input:
array = [1,2 3, 4 5]
output:
[5,4,3,2,1]
"""
# Solution 1.1:
# size of Array
size_of_array = int(input())
# creating an Array
array = [int(i) for i in input().split(' ')]
# iterating on array and print reverse array
for i in range(1, len(array) + 1):
    # printing an array using negative indexing : reference-> file_name-> negative_indexing
    print(array[-i], end=" ")

print("printing reverse array")
# for the new line
print()
# Second Solution 1.2:
"""
using two pointer solution  we will reverse a an array
Step-1: Declare a two variable one is start and send : start will be 0 and end will be length of array-1
Step2:using a while loop swap until start is less than end 
Note:
on irritation we will increment a value of start with 1 and decrement a of end with -1
"""
# this point start of array index
start_pointer = 0
# this point end of array index means last index
end_pointer = size_of_array - 1
# while loop  run until start_pointer is less than or equal to end_pointer
while start_pointer <= end_pointer:
    # swapping element at index starting to last index
    array[start_pointer], array[end_pointer] = array[end_pointer], array[start_pointer]
    # incrementing a value of start_pointer with 1
    start_pointer += 1
    # decrementing a value og end_pointer with 1
    end_pointer -= 1
# print an array now we will get reverse array
print(array)

# Solution 1.3:
"""
using a in built method that is reverse method: reverse()
"""
# reverse method will reverse your array
array.reverse()
print(array, 'using inbuilt method')

# Solution 1.4:
"""
In this we use insert method to reverse a list
Step -1 : we need to declare a empty array 
Step-2: we need to insert every element at index 0
"""
# empty list
reverse_list = []
for i in array:
    # insert every element at index 0
    reverse_list.insert(0, i)  # 0 is index and i is element
print(reverse_list, 'using insert solution')

# Solution 1.5:
"""
using a list compression
"""
reverse_list = [array[len(array) - i] for i in range(1, len(array) + 1)]
print(reverse_list)
