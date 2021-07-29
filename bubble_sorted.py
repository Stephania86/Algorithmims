
# 0(n^2)
""""
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j +1] = arr[j + 1], arr[j]

    return arr

test_data = [1, 4, 3, 6, 2]
print(test_data)
print(bubble_sort(test_data))
"""

def bubble_sort(arr):
    for i in range(len(arr)):
        print("i:" + str(i))
        for j in range(len(arr) - 1 - i):
            print("i:" + str(i))
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

# 0: [1, 4, 3, 6, 2]
# 1: [1, 4, 3, 2, 6]
# 2: [1, 3, 2, 4, 6]
# 3: [1, 2, 3, 4, 6]
# 4: [1, 2, 3, 4, 6]

test_data = [1, 4, 3, 6, 2]
print(test_data)
print(bubble_sort(test_data))