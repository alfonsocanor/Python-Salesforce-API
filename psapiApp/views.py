from psapiApp import app
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from flask_sqlalchemy import SQLAlchemy
from psapiApp import controller
import json

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/allAccountsApi' , methods=['GET', 'POST'])
def allAccountsApi():
    x=2
    accsList = controller.Queries().allAccount()
    print(accsList)
    print(type(accsList))
    return render_template('allAccountsApi.html', accsList=accsList, x=x)

#class Test(db.Model):
#    id = db.Column(db.Integer, primary_key=True)