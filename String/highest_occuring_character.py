"""
In this we need to find a highest occurring character in a given string
"""
# Problem Statement:
"""
Highest Occuring Character
Send Feedback
For a given a string(str), find and return the highest occurring character.
Example:
Input String: "abcdeapapqarr"
Expected Output: 'a'
Since 'a' has appeared four times in the string which happens to be the highest frequency character, 
the answer would be 'a'.

Sample Input 1:
abdefgbabfba
Sample Output 1:
b
Sample Input 2:
xy
"""
# Solution
# Taking user input
user_input = input()
# storing the highest occurring character
highest_occurrence = 0
# we store occurrence of every character in dict
occurrence_dict = dict()
# we store the highest_occurrence_char
highest_occurrence_char = ''
for i in user_input:
    occurrence_dict[i] = occurrence_dict.get(i, 0) + 1

# using a for loop on  occurrence_dict to find a maximum occurrence key
for key in occurrence_dict.keys():
    if highest_occurrence < occurrence_dict[key]:
        highest_occurrence_char = key
        highest_occurrence = occurrence_dict[key]
print(highest_occurrence_char)

# better solution to find a maximum occurrence
highest_occurrence_char = max(occurrence_dict, key=lambda x: occurrence_dict[x])
print(highest_occurrence_char)
