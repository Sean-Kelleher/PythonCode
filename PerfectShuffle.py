#Programmed by Sean Kelleher for CSCI 247
#3/24/17

import Mods

rank = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
suit = ['Clubs', 'Hearts', 'Diamonds', 'Spades']

def buildDeck(rank, suit):
    deck = ["%s of %s" % (r, s) for r in rank for s in suit]
    return deck

def shuffle(deck):
    half1 = deck[:26]
    half2 = deck[26:]
    newPile = []
    i = 0
    while i < 52:
        if i % 2 != 0:
            newPile.append(half1.pop())
        else:
            newPile.append(half2.pop())
        i += 1
    newPile.reverse()
    return newPile
    
def deal(deck):
    hand = deck[:5]
    return hand
    
def main():
    deck = buildDeck(rank, suit)
    i = 0;
    shuffs = Mods.promptInt("How many times do you want to shuffle?")
    while i < shuffs:
        deck = shuffle(deck)
        i += 1
    print deal(deck)
    
main()