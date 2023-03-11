"""
In this we need to remove a specific character from a given string
"""
# Problem Statement:
"""
Remove character
Send Feedback
For a given a string(str) and a character X, write a function to remove all the occurrences of X from the given string.
The input string will remain unchanged if the given character(X) doesn't exist in the input string.

Sample Input 1:
aabccbaa
a
Sample Output 1:
bccb
"""
# Taking input from a user
user_input = input()
# remove_character
remove_character = input()
# storing a result of remove character
remove_char = ''
for i in user_input:
    if i != remove_character:
        remove_char += i
print(remove_char)

