#!/usr/bin/python3

""" Author: Aleef D | Using RegEX in python """

import re

def main():
    with open("testcap.txt", "r") as testcap:
        for line in testcap:
            regmatch = re.search(r"^Contact:\ssip:\+(\d+)@\[(.*)\]:?(\d+)?" , line)
            if regmatch:
                print(regmatch)          ##display match object
                print(regmatch.group())  ##display the full match
                print("Caller ID: " + regmatch.group(1)) ##display the digits of caller
                print("IP Address: " + regmatch.group(2)) ##display the IPV6
                print("Port: " + regmatch.group(3)) ##display the port







if __name__ == "__main__":
    main()
