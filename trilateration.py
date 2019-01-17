from sympy.geometry import Circle, Point, intersection
import math


# This project was inspired by Project Lovelace. They have some science related coding
    # challenges that can be found at:
    # projectlovelace.net


# Velocity of P-waves.
v = 6.0

# Converts the coordinates from fractions to floating point numbers.
def convert_to_float(intersect, coordinate):
    firstCoord = []
    secondCoord = []
    for i in range(0, len(intersect)):
        for j in range(0, len(coordinate)):
            point = float(intersect[i][j])
            if (i > 0):
                secondCoord.append(round(point, 3))
            else:
                firstCoord.append(round(point, 3))
    return [firstCoord, secondCoord]

def earthquake_epicenter(x1, y1, t1, x2, y2, t2, x3, y3, t3):
    x = 0.0
    y = 0.0

    # The distance of each seismograph from the epicenter based on the time and the velocity.
    d1 = t1 * v
    d2 = t2 * v
    d3 = t3 * v

    # The centerpoint of each seismograph.
    coordOne = Point(x1, y1)
    coordTwo = Point(x2, y2)
    coordThree = Point(x3, y3)

    # Creates circles of possible earthquake epicenters based on the seismograph location
        # and the distance from the epicenter.
    circleOne = Circle(coordOne, d1)
    circleTwo = Circle(coordTwo, d2)
    circleThree = Circle(coordThree, d3)

    # Finds all the intercepting points of each circle.
    firstIntersect = intersection(circleOne, circleTwo)
    secondIntersect = intersection(circleOne, circleThree)
    thirdIntersect = intersection(circleTwo, circleThree)
    
    # Assign the list of floating point coordinates to a variable.
    oneAndTwoIntersect = convert_to_float(firstIntersect, coordOne)
    oneAndThreeIntersect = convert_to_float(secondIntersect, coordTwo)
    twoAndThreeIntersect = convert_to_float(thirdIntersect, coordThree)

    # Initializing the variables to test if the coordinates match. I chose to make 
        # the first list an empty string to satisfy the logic below. 
    firstCoord = ['']
    secondCoord = []
    thirdCoord = []

    # Loop over each set of coordinates in each list of sets until the conditions are met
        # and the x and y values are changed to the epicenter. 
        # firstCoord = [79.067, -27.052] | firstCoord[0] = 79.067 | firstCoord[1] = -27.052
    while (firstCoord != secondCoord and firstCoord != thirdCoord):
        for coordinateOne in oneAndTwoIntersect:
            firstCoord = coordinateOne
            for coordinateTwo in oneAndThreeIntersect:
                secondCoord = coordinateTwo
                if (firstCoord == secondCoord):
                    for coordinateThree in twoAndThreeIntersect:
                        thirdCoord = coordinateThree
                        if (secondCoord == thirdCoord):
                            x = firstCoord[0]
                            y = firstCoord[1]
    return x, y




x1 = 8.382353226
y1 = -58.003720814
t1 = 12.860754193
x2 = -13.590571819
y2 = 73.976069096
t2 = 22.847488548
x3 = 77.291172370
y3 = 7.508764456
t3 = 5.767809783


trilateration = earthquake_epicenter(x1, y1, t1, x2, y2, t2, x3, y3, t3)
print(trilateration)


