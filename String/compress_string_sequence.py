"""
In this we need to compress a given string
"""
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
# Taking input from user
user_input = input()
# compress string
compress_string = ''
count = 0
i = 0
while i < len(user_input):
    count = 1
    while i < len(user_input)-1 and user_input[i] == user_input[i+1]:
        count += 1
        i += 1
    compress_string += user_input[i]
    if count > 1:
        compress_string += str(count)
    i += 1
print(compress_string)