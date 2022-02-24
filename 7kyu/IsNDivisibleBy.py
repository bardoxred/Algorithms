# Create a function isDivisible(n,...) that checks if the first argument n is divisible by all other arguments (return true if no other arguments)

# Example:

# isDivisible(6,1,3)--> true because 6 is divisible by 1 and 3
# isDivisible(12,2)--> true because 12 is divisible by 2
# isDivisible(100,5,4,10,25,20)--> true
# isDivisible(12,7)--> false because 12 is not divisible by 7
# This kata is following kata: http://www.codewars.com/kata/is-n-divisible-by-x-and-y



def is_divisible(*args):
    num = 0
    pom = [x for x in args]
    for x in range(len(pom)-1):
        if pom[0]%pom[x+1] == 0:
            num+=1
        else: num-=1
    if num!=len(pom)-1:
        return False
    else:
        return True
    
def is_divisible(*arg):
    for i in range(1, len(arg)):
        if arg[0] % arg[i] != 0:
            return False
    return True


print(is_divisible(3,3,3))