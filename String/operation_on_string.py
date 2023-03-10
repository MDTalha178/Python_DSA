"""
In this we perform operation on a String
"""
# Split()
"""
split method is method which split a string on the basis of given argument for more clarification see the 
example and return list of split string
"""
# taking a user input
user_string = input()
# split method
new_string = user_string.split()
"""
when we not pass any argument by default it will split your string on the basis of space
"""
print(new_string)

# here we will pass argument
user_string = input()
new_string = user_string.split(' ')
print(new_string, "with Argument")

# If we want to split a string specific number of string
user_string = input()
new_string = user_string.split(' ', 1)
print(new_string)

# replace method
"""
When we want replace something in given string with other string
"""
# user input
user_string = input()
# replace word
replace_word = input()
# replace with
replace_with = input()
# using replace method
new_string = user_string.replace(replace_word, replace_with)
print(new_string)

# find method
"""
when we want something in string if that word is present in string it will return a starting index
"""
# user input
user_string = input()
# taking input which need to find
find_Word = input()
index = user_string.find(find_Word)

# lower method
"""
when we want to convert a string into lower
"""
# user input
user_string = input()
convert_string = user_string.lower()
print(convert_string)

# upper method
"""
when we want to convert a string into upper
"""
# user input
user_string = input()
convert_string = user_string.upper()
print(convert_string)