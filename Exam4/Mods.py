def findItem(dictionary, item):
    ret = ""
    for i in dictionary:
        if dictionary[i] == item:
            ret = i
    return ret;

def fileList(filename):
    file = open(filename)
    l = []
    for line in file:
        l.append(line.strip())
    return l
    
def fileListAllCaps(filename):
    file = open(filename)
    l = []
    for line in file:
        l.append(line.strip().upper())
    return l
        
def userList(prompt):
    print prompt,
    l = raw_input().split(",")
    return l

def largestFromList(l):
    # Returns -1 if it's a tie
    largest = l[0]
    tieCount = -1
    for i in l:
        if i == largest:
            tieCount += 1
        if i > largest:
            largest = i
        
    if tieCount > 0:
        largest = -1
    return largest
    
def wordPrompt(word):
    print "enter %s" % word
    return raw_input()

def printList(list):
    for word in list:
        if word in ["COOKIES", "cookies"]:
            print "_______"
        else:
            print "        " + word

def promptInt(prompt):
    print prompt,
    return int(raw_input())

def promptString(prompt):
    print prompt,
    return raw_input()

def promptFloat(prompt):
    print prompt,
    return float(raw_input)