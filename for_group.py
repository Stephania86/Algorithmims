
'''
Find max number from 3 values, entered manually from a keyboard.
Example: 124, 21, 32. Result = 124.
'''


'''
def find_max(a, b, c):
    return max(a, b, c)


n1 = int(input("Input first num: "))
n2 = int(input("Input second num: "))
n3 = int(input("Input third num: "))

print(find_max(n1, n2, n3))

'''

# 0(1)
def find_max(a, b, c):
    if a > b and a> c:
        return a
    if b > a and b > c:
        return b
    return c


n1 = int(input("Input first num: "))
n2 = int(input("Input second num: "))
n3 = int(input("Input third num: "))

print(find_max(n1, n2, n3))