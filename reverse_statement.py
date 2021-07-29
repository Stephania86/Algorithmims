# Reverse a Statement
# Build an algorithm that will print the given statement in reverse.
# Example: Initial string = Everything is hard before it is easy
# Reversed string = easy is it before hard is Everything


def reverse_sentence(s):
    word_list = s.split()
    word_list.reverse()
    reversed_sentence = " ".join(word_list)
    return reversed_sentence


str = "Everything is hard before it is easy"
print(str)
print(reverse_sentence(str))