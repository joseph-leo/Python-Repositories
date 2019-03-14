from random import randint

trials =  10000
flips = 0

for rounds in range(0, trials):
    flips += 1
    
    if (randint(0, 1) == 0):
        while (randint(0, 1) == 0):
            flips += 1
        flips += 1
    else:
        while (randint == 1):
            flips +=1
        flips += 1

print(flips / trials)
    
    
            
    
