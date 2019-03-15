import random


aWin = 0
bWin = 0

for election in range(0, 10000):
    candA = 0
    candB = 0
    regionOne = random.random()
    if (regionOne >= 0.13):
        candA += 1
    else:
        candB += 1
    regionTwo = random.random()
    if (regionTwo >= 0.35):
        candA += 1
    else:
        candB += 1
    regionThree = random.random()
    if (regionThree >= 0.83):
        candA +=1
    else:
        candB += 1
    if (candA > candB):
        aWin += 1
    else:
        bWin += 1

print("Candidate A might win {}/10,000 times, while candidate B might win {}/10,000 times.".format(aWin, bWin))
