# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 11:21:05 2020

@author: Marut
"""

from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World!"
@app.route('/predict',methods=['GET','POST'])
def predict():
    if (request.method=='GET'):
        return(jsonify({"student_predication":"Welcome to API for student prediction perfomance no use GPA university year 1 semesters 2",
                "How": "Use Post and add 10 parameter as follows",
                "Key_1":"ADMISSIONS_TYPE",
                "Key_2":"FACULTY",
                "Key_3":"SCHOOL_NAME",
                "Key_4":"ENTRY_GPA",
                "Key_5":"YEAR_COME",
                "Key_6":"STUDENT_GENDER",
                "Key_7":"FATHER_EDUCATION",
                "Key_8":"FATHER_OCUPATION",
                "Key_9":"MOTHER_EDUCATION",
                "Key_10":"MOTHER_OCUPATION"}))  
    else:
        #print(request.args.get("ADMISSIONS_TYPE"))
        return jsonify(request.get_json())

if __name__ == "__main__":
    app.run(debug=True)