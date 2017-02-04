#Programmed by Sean Kelleher for Python class

import Mods

def readTemps():
    file = open("temps.txt", "r")
    tempList = []
    for line in file:
        line = float(line)
        tempList.append(line)
    return tempList
    
def count(temps, start, stop):
    tempCount = 0
    indexCount = 0
    for temp in temps:
        indexCount += 1
        if indexCount >= start and indexCount <= stop:
            if temp > 0:
                tempCount += 1
    return tempCount

def calculateAve(temps, start, stop):
    indexCount = 0
    total = 0
    for temp in temps:
        indexCount += 1
        if indexCount >= start and indexCount <= stop:
            total += temp 
    average = total / len(temps)
    return average

#The following figures out the actual number of years that corresponds to the percentages that 
#the user is requesting. The second range is derived by subtracting from the total (116)
#to assure that it all adds up correctly.
def percent(s):
    splitted = s.split("-")
    percent1 = float(splitted[0]) / 100
    range1 = int(percent1 * 116)
    range2 = 116-range1
    ret = [range1, range2]
    return ret

def main():
    t = readTemps()
    prompt = Mods.promptString("Enter the past-future percent split you want (50-50, 60-40, 70-30 etc): ")
    ranges = percent(prompt)
    range1 = ranges[0]
    range2 = ranges[1]
    start2 = range1 + 1
    print range1
    print "During the first %i years, the average deviation from the temperature anomaly is " % range1, calculateAve(t, 0, range1)
    print "During the first %i years, %i had a positive temperature anomaly" % (range1, count(t, 0, range1))
    print "During the last %i years, the average deviation from the temperature anomaly is " % range2, calculateAve(t, start2, 116)
    print "During the last %i years, %i had a positive temperature anomaly" % (range2, count(t, start2, 116))

main()
