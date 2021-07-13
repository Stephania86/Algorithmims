'''
Compute the sum of digits in all numbers from 1 to n.
When a user enters a number n, find the sum of digits in all numbers from 1 to n.
Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15
'''



# 0(n)
def sum1(n):
    final_sum = 0
    for x in range(n + 1):
        final_sum = final_sum + x

    return final_sum


# 0(1)
def sum2(n):
    return (n * (n+ 1)) / 2


num = int(input("Input a number: "))

print(sum1(num))
print(sum2(num))

