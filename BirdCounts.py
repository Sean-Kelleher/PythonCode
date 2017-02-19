import Mods
# ------------------------------------------------------------
# For a badge do the following: 
# 
# After each user query print out the bird that has been seen 
# most often.  If there is a tie, print all of birds that are 
# tied for most sightings. 
# 
# Allow the user to enter a bird name as often as the like. 
# When they want to stop entering bird names they can type 
# 'Exit'. 
# 
# Make the lookup case insensitive.  In other words, I should 
# be able to type ROBIN or RoBiN and get the count for Robin. 
# ------------------------------------------------------------
# ------------------------------------------------------------
# Reads the specified file (filename) and returns a dictionary 
# whose keys are bird names and whose values are the number of 
# times the bird has been seen. 
# ------------------------------------------------------------
def countBirds(filename):
    file = open(filename)
    birds = {}
    for line in file:
        temp = line.split(',')
        name = temp[0].strip()
        sightings = int(temp[1].strip())
        if name not in birds:
            birds[name] = sightings
        else:
            birds[name] += sightings
    return birds
    
    
# ------------------------------------------------------------
# Asks the user to enter a bird name and then looks up 
# the sighting count for that bird in the specified 
# dictionary (d). 
# ------------------------------------------------------------
def askUser(d):
    inputName = ""
    while (inputName != 'Exit'):
        # .title() changes it to the proper capitalization format
        inputName = Mods.promptString("Enter a bird name:").title()
        if inputName == 'Exit':
            print "Bye."
        elif inputName in d:
            print "I have seen that bird %i times." % d[inputName]
        else:
            print "I have seen that bird 0 times."
        # Find the largest number in there, then get back all the birds that
        # have that number of sightings
        most = Mods.largestFromList(d.values())
        bestBirds = ""
        for name, sightings in d.items():
            if sightings == most:
                bestBirds = bestBirds + name + ", "
        print "Most Sighted Bird(s): %s" % bestBirds
    
def main():
    birds = countBirds('Birds.txt')
    askUser(birds)
    
main()
