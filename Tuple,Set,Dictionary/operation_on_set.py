"""
In this we will perform all operation of set
"""
# Declare a tuple
tuple1 = (1, 2, 3, 4)
# This also be a tuple
tuple2 = 5, 6

print(tuple1, "This Tuple 1")
print(tuple2, "This is Tuple 2")

# How to verify this element is in set or not
"""
check 1 is present in set or not this will return a boolean value means True or False
"""
# check 1
result = 1 in tuple1
print(result)
# check 2
result = 19 in tuple2
print(result)

# How to add two given set
"""
The given two tuple which add
"""
tuple3 = tuple1 + tuple2
print(tuple3, "Concatenate of two set")

# Max()
"""
When we are using inbuilt max and min data types of every which present is set should be same
"""
print(max(tuple3), "Max element in set")