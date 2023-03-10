"""
In this we check the given string is palindrome or not
"""
# Problem Statement:
"""
Check Palindrome
Send Feedback
Given a string, determine if it is a palindrome, considering only alphanumeric characters.
Palindrome:
A palindrome is a word, number, phrase, or other sequences of characters which read the same backwards
and forwards
Sample Input 1 :
abcdcba
Sample Output 1 :
true 
Sample Input 2:
coding
Sample Output 2:
false
"""
# Solution 1.1
# take input from user string
user_string = input()


def check_palindrome(user_string1: str):
    """
    check the given user string is palindrome or not
    :param user_string1:user string
    :return: boolean
    """
    start_index = 0
    end_index = len(user_string1) - 1
    while start_index < end_index:
        if user_string[start_index] != user_string1[end_index]:
            return False
        start_index += 1
        end_index -= 1
    return True


# calling function
print(check_palindrome(user_string))
