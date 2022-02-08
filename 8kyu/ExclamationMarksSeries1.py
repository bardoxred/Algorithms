# Description:
# Remove an exclamation mark from the end of a string. For a beginner kata, you can assume that the input data is always a string, no need to verify it.

# Examples
# remove("Hi!") === "Hi"
# remove("Hi!!!") === "Hi!!"
# remove("!Hi") === "!Hi"
# remove("!Hi!") === "!Hi"
# remove("Hi! Hi!") === "Hi! Hi"
# remove("Hi") === "Hi"


def remove(s):
    if len(s) > 0 and s[-1] == "!":
        return s[:-1]
    else:
        return s