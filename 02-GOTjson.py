#!/usr/bin/python3

"""Author ADavis | email: aleef.davis@live.com | Learning GOTjson.py"""

# pull in json lib so we can parse out json
import json

def main():
    # open the jonsnow.json file in read mode
    with open("jonsnow.json" , "r") as gotdata:
        jonsnow = gotdata.read() # create a STRING of all the json
        GOTpy = json.loads(jonsnow) # Convert STRING to pythonic LISTs and DICTs
    print(GOTpy) # display the GOTpy data
    print(GOTpy["url"]) # display values assoc. with URL
    print(GOTpy["titles"][0]) # display values assoc. with titles
    print(GOTpy["aliases"])

    # create a loop to move across aliases
    with open("aliases.txt", "w") as jsaliases:
        for gotalias in GOTpy["aliases"]:
            print(gotalias, file=jsaliases)

    # parse jonsnow.jason file for ...
    # display character name
    # display character alias / titles
    # display the API for ???





if __name__ == "__main__":
    main()

