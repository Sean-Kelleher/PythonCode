#Exam 6, Sean Kelleher, 4/30/17, CSI-247

import Mods

#cuts the guess out of the list
def changeList(guess, l):
    l.remove(guess) 
    return l

#Returns a list of viable suspect-weapon combinations
def possibilities(weapons, suspects):
    conclusions = []
    for w in weapons:
        for s in suspects:
            conclusions.append("%s %s" % (s, w))
    return conclusions

def main():
    weapons = ['Candlestick','Wrench','Pipe']
    suspects = ['Miss Scarlet','Col Mustard', 'Mr Green']
    conclusions = possibilities(weapons,suspects)
    print "%i possibilities left." % len(conclusions)
    while(len(conclusions) > 1):
        ws = Mods.promptString("Is the clue about a weapon or a suspect (w or s)?")
        if ws.lower() == "w":
            guess = Mods.promptString("Enter the weapon that was not used (%s):" % weapons)
            guess = guess.title() #format it properly
            weapons = changeList(guess, weapons)
        elif ws.lower() == "s":
            guess = Mods.promptString("Enter the innocent suspect (%s)" % suspects)
            guess = guess.title() #format it properly
            suspects = changeList(guess, suspects)
        conclusions = possibilities(weapons,suspects)
        print "%i possibilities left." % len(conclusions)
    print "It was %s with the %s!" % (suspects[0], weapons[0])
    
main()