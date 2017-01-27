#Programmed 1/26 by Sean Kelleher for Python
#This takes in lyrics, capitalizes the verses, lowercases the chorus, and replaces all instances of 'cookies' or 'COOKIES' with '_______'

import Mods

lyrics = []

print "Enter the first verse: ",
verse1 = raw_input().upper()
print "Enter the second verse: ",
verse2 = raw_input().upper()
print "Enter the third verse: ",
verse3 = raw_input().upper()
print "Enter the fourth verse: ",
verse4 = raw_input().upper()
print "Enter the chorus: ",
chorus = raw_input().lower()
print "Enter the chorus repeat: ",
repeat = int(raw_input())

#Multiply the chorus by the entered repeat value, then do it again +1 for the final chorus
chorusRep = (chorus + " ") * repeat
chorusExtra = (chorus + " ") * (repeat+1)

lyrics.append(verse1)
lyrics.append(chorusRep)
lyrics.append(verse2)
lyrics.append(chorusRep)
lyrics.append(verse3)
lyrics.append(chorusRep)
lyrics.append(verse4)
lyrics.append(chorusExtra)
lyrics.append("...one more time!...")
lyrics.append(verse1)
lyrics.append(chorusRep)
lyrics.append(verse2)
lyrics.append(chorusRep)
lyrics.append(verse3)
lyrics.append(chorusRep)
lyrics.append(verse4)
lyrics.append(chorusExtra)

print lyrics

Mods.printList(lyrics)