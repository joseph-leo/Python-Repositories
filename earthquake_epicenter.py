from sympy.geometry import Circle, Point, intersection
import math

# This project was inspired by Project Lovelace. They have some science related coding
    # challenges that can be found at:
    # projectlovelace.net

# In this project we also assume that the seismographs are fairly close to each other 
    # and the earthquake takes place close to the surface.

# Velocity of P-waves.
v = 6.0

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
    firstIntercepts = intersection(circleOne, circleTwo)
    secondIntercepts = intersection(circleOne, circleThree)
    thirdIntercepts = intersection(circleTwo, circleThree)
    
    # Iterate through the intercept points of the first and second circles and convert
        # the coordinates to floats. Append to either the coordinates for the first
        # intercept, or the second.
    firstCoordOne = []
    secondCoordOne = []
    for i in range(0, len(firstIntercepts)):
        for j in range(0, 2):
            point = float(firstIntercepts[i][j])
            if (i > 0):
                secondCoordOne.append(round(point, 3))
            else:
                firstCoordOne.append(round(point, 3))
    
    # Iterate through the intercept points of the first and third circles and convert
        # the coordinates to floats. Append to either the coordinates for the first
        # intercept, or the second.
    firstCoordTwo = []
    secondCoordTwo = []
    for n in range(0, len(secondIntercepts)):
        for m in range(0, 2):
            point = float(secondIntercepts[n][m])
            if (n > 0):
                secondCoordTwo.append(round(point, 3))
            else:
                firstCoordTwo.append(round(point, 3))

    # Iterate through the intercept points of the second and third circle and convert
        # the coordinates to floats. Append to either the coordinates for the first
        # intercept, or the second.
    firstCoordThree = []
    secondCoordThree = []
    for u in range(0, len(thirdIntercepts)):
        for w in range(0, 2):
            point = float(thirdIntercepts[u][w])
            if (u > 0):
                secondCoordThree.append(round(point, 3))
            else:
                firstCoordThree.append(round(point, 3))
    
    # Put the two sets of intercept coordinates in a list so that each set can be iterated 
        # over and the set can be analyzed as a whole.
    oneAndTwoIntercepts = [firstCoordOne, secondCoordOne]
    oneAndThreeIntercepts = [firstCoordTwo, secondCoordTwo]
    twoAndThreeIntercepts = [firstCoordThree, secondCoordThree]

    # Initializing the variables to test if the coordinates match. I chose to make 
        # the first list an empty string to satisfy the logic below. 
    firstCoord = ['']
    secondCoord = []
    thirdCoord = []

    # Loop over each set of coordinates in each list of sets until the conditions are met
        # and the x and y values are changed to the epicenter. 
        # firstCoord = [79.067, -27.052] | firstCoord[0] = 79.067 | firstCoord[1] = -27.052
    while (firstCoord != secondCoord and firstCoord != thirdCoord):
        for i in range(0, len(oneAndTwoIntercepts)):
            firstCoord = oneAndTwoIntercepts[i]
            for j in range(0, len(oneAndThreeIntercepts)):
                secondCoord = oneAndThreeIntercepts[j]
                if (firstCoord == secondCoord):
                    for n in range(0, len(twoAndThreeIntercepts)):
                        thirdCoord = twoAndThreeIntercepts[n]
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

earthquake = earthquake_epicenter(x1, y1, t1, x2, y2, t2, x3, y3, t3)
print(earthquake)


