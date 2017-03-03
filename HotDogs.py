#Programmed by Sean Kelleher on 3/3/17 for CSCI-247

import Mods
import random
import time

#Creates the random number of dogs eaten each loop
def eatDogs():
    tomDogs = random.randrange(1, 6)
    sallyDogs = random.randrange(1, 6)
    fredDogs = random.randrange(1, 6)
    dogsAry = [tomDogs,sallyDogs,fredDogs]
    return dogsAry

def competition():
    going = True
    eaters = {'Tom':0, 'Sally':0, 'Fred':0}
    winner = ""
    winnerName = ""
    print 'Ready, set, eat!'
    while going:
        print "\nchomp... chomp... chomp... \n"
        time.sleep(1)
        dogs = eatDogs()
        eaters['Tom'] += dogs[0]
        eaters['Sally'] += dogs[1]
        eaters['Fred'] += dogs[2]
        print "Tom has eaten %s hot dogs!" % eaters['Tom']
        print "Sally has eaten %s hot dogs!" % eaters['Sally']
        print "Fred has eaten %s hot dogs!" % eaters['Fred']
        # checks if anyone's eaten 50 or more AND if anyone's eaten more than the others
        if eaters['Fred'] >= 50 or eaters['Tom'] >= 50 or eaters['Sally'] >= 50:
            if Mods.largestFromList([eaters['Tom'], eaters['Sally'], eaters['Fred']]) > -1:
                winningScore = Mods.largestFromList([eaters['Tom'], eaters['Sally'], eaters['Fred']])
                winner = Mods.findItem(eaters, winningScore)
                going = False
    return winner

def main():
    guess = Mods.promptString("Pick a winner (Sally, Fred or Tom): ")
    winner = competition()
    if guess.title() == winner:
        print "You guessed right, %s wins!" % winner
    else:
        print "Sorry, chum, you guessed wrong. %s wins!" % winner
            
    
main()