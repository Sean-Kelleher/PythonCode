#Programmed by Sean Kelleher for CSCI 247 4/9/17
#This gets information about a few of my favorite albums from a JSON file
import json
import Mods

def getJson():
    jsonTxt = ""
    f = open('albums.json')
    for line in f:
        line = line.strip()
        jsonTxt = jsonTxt + line
    ret = json.loads(jsonTxt)
    return ret
    
def printOut(name):
    albums = getJson()
    trackCount = 1
    for album in albums:
        if album["Album"] == name.title(): #.title() makes sure that the name in the right format
            print "%s" % album["Artist"]
            for track in album["Tracks"]:
                print "%i %s" % (trackCount, track)
                trackCount += 1
def main():
    albumName = Mods.promptString("Enter an album name to see its artist and its tracklist: ")
    printOut(albumName)
    
main()
