#!/usr/bin/python3
""" author: aleef.davis@live.com | Learning about API requests """

import requests
MAJORTOM = "http://api.open-notify.orgz/astros.json"

def main():
    try:
        # make a API request
        pyj = requests.get(MAJORTOM).json()
    
        # parse out JSON we stripped off response
        astrocosmo = pyj.get("people")

        for spaceperson in astrocosmo:
        print(spaceperson["name"])
    
        # display selected data on screen - names of people in space
    except:
        print("API is unavailable at the momemt")
        exit()

if __name__ == "__main__":
    main()
