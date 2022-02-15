# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

# Note: input will never be an empty string

def fake_bin(x):
    s = list(x)
    tab = []
    new_string = ""
    for i in s:
        if int(i) < 5:
            tab.append(0)
        elif int(i) > 4:
            tab.append(1)
    for x in tab:
        new_string += str(x)
    return new_string



def fake_bin(s):
    return s.translate(string.maketrans('0123456789', '0000011111'))