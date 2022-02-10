# Can you find the needle in the haystack?

# Write a function findNeedle() that takes an array full of junk but containing one "needle"

# After your function finds the needle it should return a message (as a string) that says:

# "found the needle at position " plus the index it found the needle, so:

# find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk'])
# should return "found the needle at position 5" (in COBOL "found the needle at position 6")

def find_needle(haystack):

    for x in range(len(haystack)):
        if haystack[x] == 'needle':
            return x


print(find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]))