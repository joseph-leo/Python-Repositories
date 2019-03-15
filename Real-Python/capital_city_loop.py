from capitals import capitals_dict
import random

capitals = capitals_dict


def random_capital(capitals):
    state = random.choice(list(capitals))
    capital = capitals[state]
    correct = False
    
    while (correct == False):
        guess = input("What is the capital of " + state + ": ")
        
        guess = guess.lower()
        capital = capital.lower()

        if (guess != capital):
            continue
        else:
            print('Correct')
            break


        
        

random_capital(capitals)
