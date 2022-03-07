# Description:
# Groups of characters decided to make a battle. Help them to figure out which group is more powerful. Create a function that will accept 2 variables and return the one who's stronger.

# Rules:
# Each character have its own power: A = 1, B = 2, ... Y = 25, Z = 26
# Only capital characters can and will participate a battle.
# Only two groups to a fight.
# Group whose total power (A + B + C + ...) is bigger wins.
# If the powers are equal, it's a tie.
# Examples:
#   battle("ONE", "TWO"); // => "TWO"`
#   battle("ONE", "NEO"); // => "Tie!"

points = {
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

def battle(x, y):
    x = x.upper()
    y = y.upper()
    pom_X = x.replace("", " ").split()
    pom_Y = y.replace("", " ").split()
    x_array = []
    y_array = []
    for i in pom_X:
        if i in points:
            x_array.append(points[i])
    for j in pom_Y:
        if j in points:
            y_array.append(points[j])
    if sum(x_array) > sum(y_array):
        return x
    elif sum(x_array) == sum(y_array):
        return "Tie!"
    else:
        return y

print(battle("AAA", 'Z'))