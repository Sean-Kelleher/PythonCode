# ------------------------------------------------------
# reads the speeds in the specified file (filename)
# and returns them as a list of integers
# ------------------------------------------------------
def readData(filename):
    file = open(filename, "r")
    numList = []
    for line in file:
        line = float(line)
        numList.append(line)
    return numList
    
# ------------------------------------------------------    
# calculates and returns the average of the numbers
# in the the specified list (l)
# ------------------------------------------------------
def getAverage(l):
    total = 0
    for i in l:
        total += i
    ave = total/len(l)
    return ave
    
# ------------------------------------------------------
# counts and returns the number of values in the 
# specified list (l) that are greater than or 
# equal to maxSpeed
# ------------------------------------------------------
def countSpeeders(l, maxSpeed):
    speeders = 0
    for i in l:
        if i > maxSpeed:
            speeders += 1
    return speeders
    
# ------------------------------------------------------
# Determines the number of people speeding during 
# rush hour and not during rush hour.  Also determines
# the total fines during rush hour and not during 
# rush hour.  A person is considered speeding if they
# are traveling faster than 69 MPH.  The fine for 
# speeding during rush hour is $150.  The fine for 
# speeding not during rush hour is $100.
#
# THE CORRECT OUTPUT IS:
#
# The average speed during rush hour was 63.47.
# The average speed not during rush hour was 64.07.
# There were 4 speeders during rush hour.  Total fine = $600
# There were 6 speeders not during rush hour.  Total fine = $600
# ------------------------------------------------------
def main():
    nonRush = readData("data-not-rush.txt")
    rush = readData("data-rush.txt")
    limit = 69
    rushSpeeders = countSpeeders(rush, limit)
    nonRushSpeeders = countSpeeders(nonRush, limit)
    rushFines = 150 * rushSpeeders
    nonRushFines = 100 * nonRushSpeeders
    rushAve = getAverage(rush)
    nonRushAve = getAverage(nonRush)
    print "The average speed during rush hour was %.2f." % rushAve
    print "The average speed not during rush hour was %.2f." % nonRushAve
    print "There were %i speeders during rush hour.  Total fine = $%i" % (rushSpeeders, rushFines)
    print "There were %i speeders not during rush hour. Total fine = $%i" % (nonRushSpeeders, nonRushFines)
    
# ------------------------------------------------------
# kick off the program by calling main
# ------------------------------------------------------
main()