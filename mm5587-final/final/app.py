# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/") #main page
def main_page():
    return render_template("index.html")

@app.route("/openCV") #openCV page
def opencv():
    return "yo"

@app.route("/classes") #classespage
def classes():
    return "sup"

#start the server
if __name__ == "__main__":
    app.run()