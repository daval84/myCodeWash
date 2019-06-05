#!/usr/bin/python3
""" author: aleef.davis@live.com | learning about NASA apis and dev keys """

import requests
import pprint
MYAPI = "https://api.nasa.gov/neo/rest/v1/neo/browse?api_key="


def getkey():
    with open("/home/student/nasa.key" , "r") as keyfile:
        mykey = keyfile.read()
        return mykey.rstrip('\n')



def main():
    # harvest our key from /home/student/nasa.key
    nasakey = getkey()
    # append our key to MYAPI
    # call the API
    resp = requests.get(MYAPI + nasakey)
    asteroidz = resp.json()

    # decode json - loop across "near_earth_objects to reveal asteroids
    #print(asteroidz["near_earth_objects"])
    for bigrock in asteroidz["near_earth_objects"]:
        if bigrock["is_potentially_hazardous_asteroid"]:
            print(bigrock)
        else:
            print("This asteroid is not hazardous")
        #print

    # only display those may pose a danger to Aleef having a good weekend

if __name__ == "__main__":
    main()
