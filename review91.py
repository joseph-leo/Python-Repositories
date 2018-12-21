from random import randint

oneToss = randint(1, 6)
print(oneToss)

one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
 
for trials in range(0, 10000):
    die = randint(1, 6)
    if (die == 1):
        one += 1
    elif (die == 2):
        two += 1
    elif (die == 3):
        three += 1
    elif (die == 4):
        four += 1
    elif (die == 5):
        five += 1
    else:
        six += 1
print("One: {}, Two: {}, Three: {}, Four: {}, Five: {}, Six: {}".format(one, two, three, four, five, six))

     
