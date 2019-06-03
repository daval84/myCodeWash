
#!/usr/bin/python3
"""Author: ADavis | Email: aleef.davis@live.com | Learning JSON with python"""

# python has no json support
# with python, the jsonbatteries are in the box, but you need to plug them in
import json

def main():
    videogames = [{"game1": "COD 3" , "game2":"Battlefield", "game3":"Final Fantasy", "game4":"Resident Evil"} , {"game1":"Paperboy" , "game2":"Donkey Kong"}]
    
    # show the value of videogames
    print(videogames)

    # create a local file
    with open("videogames.json", "w") as vidfile: # "w" = write, "r" = read, "a" = append
        json.dump(videogames, vidfile)


if __name__ == "__main__":
    main()



