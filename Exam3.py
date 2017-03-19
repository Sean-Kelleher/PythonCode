#---------
# By Sean Kelleher for CSCI247.
#---------

import random
import Mods

#This takes the user's choices and the choices, verifies the choices are real
#returns a string saying what the chosen cards were
#and a boolean regarding whether the game should keep going or not

def verify(num1, num2, choices):
    ret = {'go': True, 'str': ""}
    winning = ""
    if num1 < 0 or num1 > 9 or num2 < 0 or num2 > 9 or num2 == num1:
        ret['str'] = "Invalid choices. you must pick different cards and the card must be a number from 0-9"
    else:
        ret['str'] = "Card %i is a %s. \nCard %i is a %s" % (num1, choices[num1], num2, choices[num2])
        if choices[num1] == choices[num2]:
            ret['go'] = False
    return ret

#This adds a duplicate of a random element to the end of the list, then shuffles it
def processAry(ary):
    chosen = random.randint(0,8)
    dupe = ary[chosen]
    ary.append(dupe)
    random.shuffle(ary)

def main():
    tries = 0
    going = True
    choices= ['bird','dog','snake','fish','cat','mouse','starfish','woodchuck','crab']
    processAry(choices)
    while going:
        card1 = Mods.promptInt('Pick the first card to turn over (0-9):')
        card2 = Mods.promptInt('Pick the second card to turn over (0-9):')
        tries += 1
        result = verify(card1, card2, choices)
        print result['str']
        going = result['go']
    print 'You win! It took you %i tries.' % tries
    
main()