
def largestFromList(l):
    largest = l[0]
    for i in l:
        if i > largest:
            largest = i
    return largest
    
def wordPrompt(word):
    print "enter %s" % word
    return raw_input()

def printList(list):
    for word in list:
        if word in ["COOKIES", "cookies"]:
            print "_______"
        else:
            print word

def promptInt(prompt):
    print prompt,
    return int(raw_input())

def promptString(prompt):
    print prompt,
    return raw_input()

def promptFloat(prompt):
    print prompt,
    return float(raw_input)