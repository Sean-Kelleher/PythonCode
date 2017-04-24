#programmed by Sean Kelleher on 4/23/17 for CSCI 247
#Assignment 8 (Weather)
import json
import urllib
import Mods

def getJson(location):
    q = str(location)
    url = "https://api.apixu.com/v1/current.json?key=85e6c07c14ba4720b6c220503172304&q=" + q
    jsonTxt = ""
    f = urllib.urlopen(url)
    for line in f:
        line = line.strip()
        jsonTxt = jsonTxt + line
    ret = json.loads(jsonTxt)
    return ret
    
def interpret(info, location):
    print "Here is the current weather for %s" % location
    temperature = info['current']['temp_f']
    condition = info['current']['condition']['text']
    feel = info['current']['feelslike_f']
    print "%s and %s degrees (F)." % (condition, temperature)
    print "It actually feels like %s degrees (F)." % feel
    
def main():
    done = False
    while(done == False):
        location = Mods.promptString("Please enter a zipcode or city name: ")
        info = getJson(location)
        interpret(info, location)
        yn = Mods.promptString("Want to check another location? (y/n)")
        if(yn == "n"):
            done = True
    
main()