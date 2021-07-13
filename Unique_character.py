'''
Unique Characters in String
Given a string, determine if it consists of all unique characters.
For example, the string 'abcde' has all unique characters and should return True.
The string 'aabcde' contains duplicate characters and should return False.
'''

def uni_char(s): # abcde length = 5
    my_set = set(s) # {a, b, c, d, e} length = 5
    return len(s) == len(my_set)

print(uni_char("abcde")) # True
print(uni_char("aabcde")) # False