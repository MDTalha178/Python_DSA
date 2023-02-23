# define a list
li = [1, 2, 3, 4]

# positive index
"""Access an with positive index.
   when we access an element with positive index it will give an element from starting
"""
print(li[1], "Access an element with positive positive index")

# negative index
"""Access an element with negative negative index
   when we access an element with negative index it will give an element from ending
"""
print(li[-1], "Access an element with negative index")

# sequencing
"""There is various ways to access an element from a list
   it works with this structure:
   list = [start_index, end_index, step]
"""
print(li[1:], end=" ")
print("it will all element from index 1 to last index")

"""it will give you all elements from index 1 to last index
"""
print(li[1:4:1])

"""it will give you all elements from index 1 to last index but skip every next elemnt
"""
print(li[1:4:2])
