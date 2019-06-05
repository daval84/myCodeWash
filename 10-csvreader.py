#!/usr/bin/python3


import csv
import json

def main():
    # open a file to dump json to
    jsonf = open('superhero.json' , 'w')

    # open our csv file to read in CSV to python format
    with open('superhero.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        #for row in reader:
        json.dump(list(reader), jsonf):

    jsonf.close() # close the superhero.json file we opened

if __name__ == "__main__":
    main()
