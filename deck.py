from random import shuffle
import time

# Function to create and shuffle deck.
def deck():
    deck = []
    for suit in ['H', 'S', 'C', 'D']:
        for rank in ['A', '2', '3', '4', '5', '6',
                     '7', '8', '9', 'T', 'J', 'Q', 'K']:
            deck.append(rank+suit)
    shuffle(deck)
    return deck

# Function to give initial cards.
def createHand(myDeck):
    yourHand = []
    dealersHand = []

    yourHand.append(myDeck.pop())
    yourHand.append(myDeck.pop())

    dealersHand.append(myDeck.pop())
    dealersHand.append(myDeck.pop())

    return [yourHand, dealersHand]

# Function to find the value of the dealers first card.
def dealersFirst(dealersHand):
    firstCardTotal = 0
    if (dealersHand[0][0] == 'T' or dealersHand[0][0] == 'J'
        or dealersHand[0][0] == 'Q' or dealersHand[0][0] == 'K'):
        firstCardTotal += 10
    elif (dealersHand[0][0] != 'A'):
        firstCardTotal += int(dealersHand[0][0])
    elif (dealersHand[0][0] == 'A'):
        firstCardTotal = 11
    return firstCardTotal

# Function to add additional points to the dealers hand.
def dealersTotalPoints(dealersHand, firstCardTotal):
    dealerTotal = 0
    dealerTotal += firstCardTotal
    for i in range(1, len(dealersHand)):
        if (dealersHand[i][0] == 'T' or dealersHand[i][0] == 'J'
            or dealersHand[i][0] == 'Q' or dealersHand[i][0] == 'K'):
            dealerTotal += 10
        elif (dealersHand[i][0] != 'A'):
            dealerTotal += int(dealersHand[i][0])
        elif (dealerTotal > 10 and dealersHand[i][0] == 'A'):
            dealerTotal += 1
        else:
            dealerTotal += 11
    return dealerTotal

# Find the points of the users cards
def userTotalPoints(yourHand):
    userTotal = 0
    for i in range(0, len(yourHand)):
        if (yourHand[i][0] == 'T' or yourHand[i][0] == 'J'
            or yourHand[i][0] == 'Q' or yourHand[i][0] == 'K'):
            userTotal += 10
        elif (yourHand[i][0] != 'A'):
            userTotal += int(yourHand[i][0])
        elif (yourHand[i][0] == 'A' and userTotal > 10):
            userTotal += 1
        else:
            userTotal += 11
    return userTotal
            





game = True
while (game == True):
    gameOver = False
    time.sleep(.5)
    start = input('Play now (y/n): ')
    if (start != 'y'):
        print('Okay bye')
        break
    else:
        print('\n')
        print('Dealing cards.')
        print('\n')
        time.sleep(1)
        innerLoop = True
        while (innerLoop == True):
            
            myDeck = deck()

            hand = createHand(myDeck)

            yourHand = hand[0]
             
            yourPoints = userTotalPoints(yourHand)
            
            dealersHand = hand[1]
            dealersFirstCard = dealersHand[0]

            dealersFirstPoints = dealersFirst(dealersHand)
            dealersTotal = dealersTotalPoints(dealersHand, dealersFirstPoints)

            print('The Dealer has: ')
            print(dealersFirstCard)
            print(str(dealersFirstPoints) + ' points.')
            print('\n')
            time.sleep(1)
            print('You have: ')
            print(yourHand[0] + ' and ' + yourHand[1])
            print(str(yourPoints) + ' points.')
            print('\n')
            if (yourPoints == 21):
                time.sleep(1)
                print('Blackjack! You win!')
                print('\n')
                gameOver = True
                continue
            elif (dealersFirstPoints == 11):
                print('Dealer has Ace.')
                print('\n')
                time.sleep(1)
                print('Checking for blackjack.')
                print('\n')
                time.sleep(1)
                print('The Dealer has: ')
                print(dealersHand[0] + ' and ' + dealersHand[1])
                print(str(dealersTotal) + ' points.')
                print('\n')
                time.sleep(1)
                print('You have: ')
                print(yourHand[0] + ' and ' + yourHand[1])
                print(str(yourPoints) + ' points.')
                print('\n')
                if (dealersTotal == 21):
                    time.sleep(1)
                    print('Blackjack! Dealer wins.')
                    print('\n')
                    myDeck.extend(yourHand)
                    myDeck.extend(dealersHand)
                    gameOver = True
                    continue
            time.sleep(1)
            hitOrStand = input("'H' for hit, or 'S' for stand: ").lower()
            while (hitOrStand == 'h'):
                yourHand.append(myDeck.pop())
                yourPoints = userTotalPoints(yourHand)
                print('\n')
                print('Drawing.')
                print('\n')
                time.sleep(1)
                if (yourPoints < 21):
                    print('The Dealer has: ')
                    print(dealersFirstCard)
                    print(str(dealersFirstPoints) + ' points.')
                    print('\n')
                    time.sleep(1)
                    print('You have: ')
                    print(yourHand)
                    print(str(yourPoints) + ' points.')
                    print('\n')
                    hitOrStand = input("'H' for hit, or 'S' for stand: ").lower()
                    time.sleep(1)
                elif (yourPoints == 21):
                    print('The Dealer has: ')
                    print(dealersHand[0] + ' and ' + dealersHand[1])
                    print(str(dealersTotal) + ' points.')
                    print('\n')
                    time.sleep(1)
                    print('You have: ')
                    print(yourHand)
                    print(str(yourPoints) + ' points.')
                    print('\n')
                    time.sleep(1)
                    print('Blackjack! You Win.')
                    print('\n')
                    gameOver = True
                    hitOrStand = ''
                elif (yourPoints > 21 and gameOver == False):
                    myDeck.extend(yourHand)
                    myDeck.extend(dealersHand)
                    print('The Dealer has: ')
                    print(dealersHand[0] + ' and ' + dealersHand[1])
                    print(str(dealersTotal) + ' points.')
                    print('\n')
                    time.sleep(1)
                    print('You have: ')
                    print(yourHand)
                    print(str(yourPoints) + ' points.')
                    print('\n')
                    time.sleep(1)
                    print('Bust! Dealer wins.')
                    print('\n')
                    gameOver = True
                    hitOrStand = ''
            while (dealersTotal < 16 and dealersTotal < yourPoints and gameOver == False):
                dealersHand.append(myDeck.pop())
                dealersTotal = dealersTotalPoints(dealersHand, dealersFirstPoints)
                print('\n')
                print('Dealer drawing')
                print('\n')
                time.sleep(1)
                if (dealersTotal < 16):
                    print('The Dealer has: ')
                    print(dealersHand)
                    print(str(dealersTotal) + ' points.')
                    print('\n')
                    time.sleep(1)
                    print('You have: ')
                    print(yourHand)
                    print(str(yourPoints) + ' points.')
                    print('\n')                    
            if (dealersTotal > 21 and gameOver == False):
                print('The Dealer has: ')
                print(dealersHand)
                print(str(dealersTotal) + ' points.')
                print('\n')
                time.sleep(1)
                print('You have: ')
                print(yourHand)
                print(str(yourPoints) + ' points.')
                print('\n')
                time.sleep(1)
                print('Dealer busts! You win!')
                print('\n')
                gameOver = True
            elif (yourPoints > dealersTotal and gameOver == False):
                time.sleep(.5)
                print('\n')
                print('The Dealer has: ')
                print(dealersHand)
                print(str(dealersTotal) + ' points.')
                print('\n')
                time.sleep(1)
                print('You have: ')
                print(yourHand)
                print(str(yourPoints) + ' points.')
                print('\n')
                time.sleep(1)
                print('You win!')
                print('\n')
                gameOver = True
            elif (dealersTotal > yourPoints and gameOver == False):
                time.sleep(.5)
                print('The Dealer has: ')
                print(dealersHand)
                print(str(dealersTotal) + ' points.')
                print('\n')
                time.sleep(1)
                print('You have: ')
                print(yourHand)
                print(str(yourPoints) + ' points.')
                print('\n')
                time.sleep(1)
                print('Dealer wins.')
                print('\n')
                gameOver = True
            innerLoop = False
         
     
     




    
