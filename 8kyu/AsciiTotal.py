# You'll be given a string, and have to return the sum of all characters as an int. The function should be able to handle all ASCII characters.

# examples:

# uniTotal("a") == 97 uniTotal("aaa") == 291

def uni_total(s):
    if not s:
        return 0
    else:
        return sum([ord(chr) for chr in s])


print(uni_total('ifkhchlhfd'))