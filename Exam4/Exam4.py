#Exam 4
#Programmed by Sean Kelleher 4/2/17 for CSCI-247

import os
import Mods

#This gets you a dictionary of {filename: an array of the file's lines}
#after sorting out the .txt files alone
def getFileContents():
    flist = []
    files = os.listdir(".")
    for f in files:
        if '.txt' in f:
            flist.append(f)
    contentsDict = {}
    for f in flist:
        contentsDict[f] = Mods.fileListAllCaps(f)
    return contentsDict

#Searches throughout the aforementioned dictionary
def searchFiles(term, files):
    ret = []
    names = []
    found = 0
    for f in files:
        names.append(f)
    for f in files:
        for line in files[f]:
            if term in line:
                found += 1   
                ret.append(f + ": " + line)
    ret.insert(0, 'I found ' + str(found) + ' results.')
    return ret

def main():
    contentsDict = getFileContents()
    term = Mods.promptString('Enter a search term: ')
    searched = searchFiles(term.upper(), contentsDict)
    for s in searched:
        print s
    
main()
    