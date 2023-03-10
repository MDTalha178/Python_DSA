"""
Tn this we find the string1 and string2 are indetical each other or not
"""
# Problem Statement:
"""
Check Permutation
Send Feedback
For a given two strings, 'str1' and 'str2', check whether they are a permutation of each other or not.
Permutations of each other
Two strings are said to be a permutation of each other when either of the string's characters can be 
rearranged so that it becomes identical to the other one.

Example: 
str1= "sinrtg" 
str2 = "string"

Sample Input 1:
abcde
baedc
Sample Output 1:
true
Sample Input 2:
abc
cbd
Sample Output 2:
false
"""
# Solution
# taking user input
user_input1 = input()
# taking second input
user_input2 = input()


def check_permutation(string: str, string2: str):
    """
    check whether the given string is permutation each other or not
    :param string: string1
    :param string2: string2
    :return: boolean value True or false
    """
    # we need to sort fist
    sort_string1 = sorted(string)
    # we need to sort second string
    sort_string2 = sorted(string2)
    for i in range(len(sort_string1)):
        if sort_string2[i] != sort_string1[i]:
            return False
    return True


# calling method
print(check_permutation(user_input1, user_input2))
