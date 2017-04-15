#Exam 5, programmed 4/15 by Sean Kelleher for CSCI-247

import json
import Mods

#opens the json file and processes its contents
def getJson():
    jsonTxt = ""
    f = open('PetStore.json')
    for line in f:
        line = line.strip()
        jsonTxt = jsonTxt + line
    ret = json.loads(jsonTxt)
    return ret

#takes in a search term and whether it's looking for keyword or category
def search(term, searchtype):
    term = term.title() #.title() makes it so that the capitalization is right
    searchtype = searchtype.title()
    petstore = getJson()
    if searchtype == "Category":
        for product in petstore:
            if product["Category"] == term:
                print product["Product"] + " - $" + str(product["Price"])
    elif searchtype == "Keyword":
        for product in petstore:
            if term in product["Product"]:
                print product["Product"] + " - $" + str(product["Price"])
    
def main():
    ck = Mods.promptString("Search by category (c) or keyword (k)?")
    searchtype = ""
    if ck.lower() =='c':
        searchtype = "category"
    elif ck.lower() == 'k':
        searchtype = "keyword"
    term = Mods.promptString("Enter a %s:" % searchtype)
    search(term, searchtype)
    
main()