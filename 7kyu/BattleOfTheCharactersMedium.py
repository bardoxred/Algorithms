# Groups of characters decided to make a battle. Help them to figure out what group is more powerful. Create a function that will accept 2 variables and return the one who's stronger.

# Rules
# Each character has its own power:
#   A = 1, B = 2, ... Y = 25, Z = 26
#   a = 0.5, b = 1, ... y = 12.5, z = 13
# Only alphabetical characters can and will participate in a battle.
# Only two groups to a fight.
# Group whose total power (a + B + c + ...) is bigger wins.
# If the powers are equal, it's a tie.
# Examples
# "One", "Two"  -->  "Two"
# "ONE", "NEO"  -->  "Tie!"
upper_case = {
    'A' : 1,
    'B' : 2,
    'C' : 3,
    'D' : 4,
    'E' : 5,
    'F' : 6,
    'G' : 7,
    'H' : 8,
    'I' : 9,
    'J' : 10,
    'K' : 11,
    'L' : 12,
    'M' : 13,
    'N' : 14,
    'O' : 15,
    'P' : 16,
    'Q' : 17,
    'R' : 18,
    'S' : 19,
    'T' : 20,
    'U' : 21,
    'V' : 22,
    'W' : 23,
    'X' : 24,
    'Y' : 25,
    'Z' : 26
}
lower_case = {
    'a' : 0.5,
    'b' : 1,
    'c' : 1.5,
    'd' : 2,
    'e' : 2.5,
    'f' : 3,
    'g' : 3.5,
    'h' : 4,
    'i' : 4.5,
    'j' : 5,
    'k' : 5.5,
    'l' : 6,
    'm' : 6.5,
    'n' : 7,
    'o' : 7.5,
    'p' : 8,
    'q' : 8.5,
    'r' : 9,
    's' : 9.5,
    't' : 10,
    'u' : 10.5,
    'v' : 11,
    'w' : 11.5,
    'x' : 12,
    'y' : 12.5,
    'z' : 13
}

def battle(x: str, y: str) -> str:
    pom_X = x.replace("", " ").split()
    pom_Y = y.replace("", " ").split()
    x_array = []
    y_array = []
    for i in pom_X:
        if i in upper_case:
            x_array.append(upper_case[i])
        elif i in lower_case:
            x_array.append(lower_case[i])
            
    for j in pom_Y:
        if j in upper_case:
            y_array.append(upper_case[j])
        elif j in lower_case:
            y_array.append(lower_case[j])

    if sum(x_array) > sum(y_array):
        return x
    elif sum(x_array) == sum(y_array):
        return "Tie!"
    else:
        return y


def battle(x,y):
    sum_x, sum_y = sum(ord(i)-64 if i.isupper() else (ord(i)-96)*0.5 for i in x), sum(ord(i)-64 if i.isupper() else (ord(i)-96)*0.5 for i in y)
    return x if sum_x>sum_y else y if sum_x<sum_y else "Tie!"
    
print(battle("Foo", "BAR"))