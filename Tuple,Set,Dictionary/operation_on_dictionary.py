"""
In this perform all operation on dictionary
"""
# Declare dictionary
first_dict = {1: 1, 2: 3, 'age': 24, 'tech': 'python'}

# Accessing an element using key
"""
When we Accessing an element using key what ever the value of key will return
"""
print(first_dict['age'], 'Accessing an element using key')

# get()
"""
get method is one of the method to access an element from dictionary . if key is present in dictionary
it will return a value of key if not present it will return None
Note:
If key is not present in dictionary by default get() method will return None but we cal also provide a custom
value which will if key is not present in dictionary
"""
# Accessing a valid key
print(first_dict.get('age'), 'Access an element with a Invalid key using get method')

# Accessing a Invalid key
print(first_dict.get('invalid'), 'Access an element with a Invalid key using get method')

# Accessing an Invalid key  with custom value
print(first_dict.get('invalid', 'Not Present'), 'Access an element with a Invalid key using get method by passing a custom value')

# Get all keys using keys()
"""
If you want to get all keys from a dictionary
"""
print(first_dict.keys(), 'Get all keys using keys() method')

# Get all values using values()
"""
if you want to get all values from a dictionary using values() method
values(): This method will return all values of dictionary
"""
print(first_dict.values(), 'Get all values using values() method')

# Get all key value pair using items()
"""
if you want to get all key value items from dictionary using items() method
items():This method will return all key value pair  which present in dictionary 
"""
print(first_dict.items(), 'Get all keys values using items() method')