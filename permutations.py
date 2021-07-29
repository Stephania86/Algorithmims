# Permutations
# Write a solution that will print all permutations of a string.
# A permutation is an act of changing the arrangement of characters.
# Example: String = ABC, Return {ABC, ACB, BAC, BCA, CBA, CAB}





def permute(a, l, r):
    if l == r:
        print(''.join(a))
    else:
        for i in range(l, r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l] # backtrack


permute(['A', 'B', 'C'], 0, (len(['A', 'B', 'C'])-1))