"""
In this we perform all operation on dictionary
"""
# How to declare a dictionary
declare_empty_dict = {}

# Declare a dictionary with element
declare_empty_dict_with_element = {'Name': 'MD Talha', 'Age': 24, 'Teach Stack': 'Python'}
print(declare_empty_dict_with_element)

# How copy all element of dictionary in other dictionary
copy_dict = declare_empty_dict_with_element.copy()
print(copy_dict, "Dictionary with copy")

"""
we cal also insert a element by using tuple and list
"""
using_list_tuple_dict = dict([('a', 10), ('b', 20), ('c', 90)])
print(using_list_tuple_dict, "Making dictionary using Tuple and List")

# How to use fromkeys function
"""
we can create a key for a dictionary using fromkeys function
"""
using_from_keys_func = dict.fromkeys(['abc', 1, 2, 'xyz'])
print(using_from_keys_func, "using from keys function")
