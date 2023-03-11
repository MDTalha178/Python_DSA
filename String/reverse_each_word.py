"""
In this we need to reverse each word of a given string
"""
# Problem statement
"""
Reverse Each Word
Send Feedback
Aadil has been provided with a sentence in the form of a string as a function parameter. The task is to implement a function so as to print the sentence such that each word in the sentence is reversed.
Example:
Input Sentence: "Hello, I am Aadil!"
The expected output will print, ",olleH I ma !lidaA".

Sample Input 1:
Welcome to Coding Ninjas
Sample Output 1:
emocleW ot gnidoC sajniN
"""
# Solution:
# Taking input from user
user_input = input()

# first split every word
split_word = user_input.split(' ')

# storing a reverse of each word
reverse_each_word = ''
for i in split_word:
    start_point = 0
    end_point = len(i) - 1
    while start_point < len(i):
        reverse_each_word += i[end_point]
        start_point += 1
        end_point -= 1
    reverse_each_word += ' '

print(reverse_each_word)
