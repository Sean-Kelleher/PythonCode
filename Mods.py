def wordPrompt(word):
    print "enter %s" % word
    return raw_input()

def printList(list):
    for word in list:
        if word in ["COOKIES", "cookies"]:
            print "_______"
        else:
            print word