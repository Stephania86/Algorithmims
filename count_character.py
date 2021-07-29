# Count Characters
# Create a program that will count vowels and consonants in a string.
# Example: String = “hello world”, Return {Vowels: 3, Consonants: 7}
# vowels: aeiou

def count_characters(s):
    vowels = 0
    consonants = 0

    for i in s:
        if i == " ":
            continue
        if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or
                 i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
            vowels += 1
        else:
            consonants += 1
    return f"Vowels: {vowels}, Consonants: {consonants}"

print(count_characters("hello world"))

