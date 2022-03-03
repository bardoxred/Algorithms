# In this Kata the aim is to compare each pair of integers from 2 arrays, and return a new array of large numbers.

# Note: Both arrays have the same dimensions.

# Example:

# arr1 = [13, 64, 15, 17, 88]
# arr2 = [23, 14, 53, 17, 80]
# get_larger_numbers(arr1, arr2) == [23, 64, 53, 17, 88]

def get_larger_numbers(a, b):
    new_array = []
    for x in range(len(a)):
        if a[x] >= b[x]:
            new_array.append(a[x])
        else:
            new_array.append(b[x])
        
    return new_array

def get_larger_numbers(a, b):
    return map(max, a, b)