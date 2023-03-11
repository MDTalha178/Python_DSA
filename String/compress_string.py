"""
In this we need to compress a given string
"""
# Problem Statement
"""
Compress the String
Send Feedback
Write a program to do basic string compression. For a character which is consecutively repeated more 
than once, replace consecutive duplicate occurrences with the count of repetitions.

Sample Input 1:
aaabbccdsa
Sample Output 1:
a3b2c2ds
"""
# Taking a user input
user_input = input()

# we store a compress string
compress_string = ''
# count of every character
count_every_character = dict()

for i in user_input:
    count_every_character[i] = count_every_character.get(i, 0) + 1

for i in count_every_character.items():
    compress_string += str(i[0])
    compress_string += str(i[1])
print(compress_string)