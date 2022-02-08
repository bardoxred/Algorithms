# Given an array of integers.

# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

# If the input array is empty or null, return an empty array.

# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

def count_positives_sum_negatives(arr):
    sum = 0
    count = 0
    if len(arr) == 0:
        return []
    for x in arr:
        if x < 0:
            sum += x
        elif x > 0:
            count+=1
    return [count, sum]