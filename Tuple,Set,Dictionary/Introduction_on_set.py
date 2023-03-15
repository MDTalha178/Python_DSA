"""
In this we will se about set
"""
# SET
"""
set is a data structure in python which store multiple type of data and unique data and unordered
Note:
set store only unique element
"""
# How to declare an empty set
declare_empty_set = set()

# How to store an element in a set
"""
here we try to store an element in a set and we try store a duplicate element
Note:
set will consider only a unique element
"""
data_set = {1, 2, 3, 3, 2, 5, 6, 1}
print(data_set, "You will get only unique element")

# How add some data in existing set
"""
We need to use add() method to insert a new element in a set
"""
data_set.add(7)
print(data_set, "Here we use add method to insert a new element")

# Note:
"""
when try to insert a new element in a set which is already present in a set that element will ignore
"""
data_set.add(7)
print(data_set, " Try to insert a new element in a set which is already present")