# Task
# Your challenge is to write a function named getSlope/get_slope/GetSlope that calculates the slope of the line through two points.

# Input
# Each point that the function takes in is an array 2 elements long. The first number is the x coordinate and the second number is the y coordinate. If the line through the two points is vertical or if the same point is given twice, the function should return null/None.

def getSlope(p1, p2):
    delta_x = p2[0] - p1[0]
    delta_y = p2[1] - p1[1]
    slop = delta_y / delta_x
    
    if p1[0] == p2[0]:
        return None
    else:
        return slop