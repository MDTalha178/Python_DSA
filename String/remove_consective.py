"""
In this we need remove a connective duplicate in a given string
"""
# Problem Statement:
"""
Remove Consecutive Duplicates
For a given string(str), remove all the consecutive duplicate characters.
Example:
Input String: "aaaa"
Expected Output: "a"

Input String: "aabbbcc"
Expected Output: "abc"
"""
# Solution
# taking user input
user_input = input()
# storing a final result
result_string = ''
# for loop to make result_string
for i in user_input:
    if i not in result_string:
        result_string += i
print(result_string)
