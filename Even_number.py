'''
Count odd and even numbers. Count odd and even digits of the whole number.
Example: entered number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).
'''




def count_odd_even(n):
    odds = 0
    evens = 0

    for current_digit in str(n):
        if int(current_digit) % 2:
            odds += 1
        else:
            evens += 1


    return ["Evens: " + str(evens), "Odds: " + str(odds)]

num = int(input("Input a number: "))
print(count_odd_even(num))