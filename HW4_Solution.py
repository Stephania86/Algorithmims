# Below The Arithmetical Mean
# When given a list, the program should return a list of all the elements below the original list’s arithmetical mean.
# The arithmetical mean is the sum of all elements divided by the number of elements.
# Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]


def below_or_mean(arr):
    ar_mean = sum(arr) / len(arr)
    print("Ar. mean: " + str(ar_mean))
    final_list = []
    for i in arr:
        if i < ar_mean:
            final_list.append(i)
    return final_list


test_array = [1, 3, 5, 6, 4, 10, 2, 3]
print(test_array)
print(below_or_mean(test_array))


