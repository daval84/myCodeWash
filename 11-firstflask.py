#!/usr/bin/python3

""" Author: Aleef"""

from flask import Flask
app = Flask(__name__) # ALWAYS do this in your flask script

@app.route("/") # When you goto the ROOT of your server... do the following
def endoftheday(): # function to trigger at ROOT
    return "Class is nearing the end for Wednesday" # RETURN this if you goto ROOT


@app.route("/hello/<name>", defaults={'position': 'Administrative Assistant'})
@app.route("/hello/<name>/<position>")
def hellostudents(name, position):
    return "Hello {1} {0}. I am pleasd to meet you {0}".format(name, position)
    #return 


if __name__ == "__main__":
    app.run(port=5006) # run on port 5006
