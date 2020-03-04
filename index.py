# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 17:59:41 2020

@author: Marut
"""

from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World!"
if __name__ == "__main__":
    app.run()