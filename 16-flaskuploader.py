# -*- coding: utf-8 -*-
#!/usr/bin/python3

"""Author: daval84"""

#These are standard libraries
import re
import json
import smtplib
from email.message import EmailMessage

from flask import Flask, render_template, request, redirect, url_for
from werkzeug import secure_filename


app = Flask(__name__)

@app.route("/upload")
def uploadfile():
    return render_template("upload.html")

@app.route("/uploader" , methods = ["POST"])
def uploader():
    if request.method == "POST":
        mysteryfile = request.files["file"]
        mysteryfile.save(secure_filename(mysteryfile.filename))
        if "cap" in mysteryfile.filename:
            return redirect(url_for("sip", filetoparse = mysteryfile.filename))
        else:
            return "That format is not yet supported. Please check back soon."

@app.route("/sip/<filetoparse>")
def sip(filetoparse):
    sipjson = []
    with open(filetoparse) as capture:
        for line in capture:
            matchobj = re.search(r"sip:\+(\d+)@\[(.*)\]:?(\d+)", line)
            if matchobj:
                tinylist = []
                tinylist.append(matchobj.group())
                tinylist.append(matchobj.group(1))
                tinylist.append(matchobj.group(2))
                tinylist.append(matchobj.group(3))
                sipjson.append(tinylist)
        return json.dumps(sipjson)

@app.route("/emailsender")
def emailsender():
    msg = EmailMessage()
    msg['Subject'] = "This is Aleef subject line"
    msg['From'] = "pythonstudent01mail.com"
    msg['To'] = "rzfeeserspam@gmail.com"
    msg.preamble = "Hey you just got a message from Aleef, Captain Jamerica"

    with open("/home/student/emailpassword.txt") as emailpass:
        myemailpass = emailpass.read()
        
    mail = smtplib.SMTP("smtp.mail.com" , 587)
    mail.starttls()
    mail.login("pythonstudent01@mail.com", myemailpass)
    mail.sendmail("pythonstudent01@mail.com", "rzfeeserspam@gmail.com", msg.as_string())
    mail.quit()
    return "Spammity spamcakes sent"

if __name__ == "__main__":
    app.run(port=5006)
