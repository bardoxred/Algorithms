# In this simple exercise, you will create a program that will take two lists of integers, a and b. Each list will consist of 3 positive integers above 0, representing the dimensions of cuboids a and b. You must find the difference of the cuboids' volumes regardless of which is bigger.

# For example, if the parameters passed are ([2, 2, 3], [5, 4, 1]), the volume of a is 12 and the volume of b is 20. Therefore, the function should return 8.

# Your function will be tested with pre-made examples as well as random ones.

# If you can, try writing it in one line of code.
from numpy import prod

def find_difference(a, b):
    sum1, sum2 = 1, 1
    for x in a:
        sum1 *= x
    for x in b:
        sum2 *= x

    return abs(sum1-sum2)

def find_difference(a, b):
    return abs(prod(a) - prod(b))


    