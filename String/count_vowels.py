"""
In this we need count  a vowels in a given string
"""
# Problem Statement
"""
In a given string we need to find how many vowels are present in the given String
Input: 
'abcdeuiss'
output:
3 there 3 vowels present in a given string
"""
# solution:
# taking a user input:
user_input = input()
# declaring a constant vowels list which store all 5 vowels
VOWELS_LIST = ['a', 'e', 'i', 'o', 'u']
# storing a count of vowels
vowels_count = 0
for i in user_input:
    if i in VOWELS_LIST:
        vowels_count += 1
print(vowels_count)


