#!/usr/bin/python3

import csv

def main():
    with open('superhero.csv' , newline = '') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['heroname'] , "is" , row['name'])


if __name__ == "__main__":
    main()
