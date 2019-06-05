#!/usr/bin/python3
""" author: aleef.davis@live.com | Learning about API requests """

import json
import urllib.request

MAJORTOM = "http://api.open-notify.org/astros.json"

def main():
    # make a API request
    resp = urllib.request.urlopen(MAJORTOM)
    
    # make python strip json data FROM the 200 response
    jstring = resp.read()
    
    # convert strin data to JSON
    pyj = json.loads(jstring.decode('utf-8'))
    
    # parse out JSON we stripped off response
    astrocosmo = pyj.get("people")

    for spaceperson in astrocosmo:
        print(spaceperson["name"])
    
    # display selected data on screen - names of people in space

if __name__ == "__main__":
    main()
