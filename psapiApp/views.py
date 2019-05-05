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

@app.route('/test' , methods=['GET', 'POST'])
def test():
    x = controller.Queries().allAccount()
    print(type(x))
    return render_template('test.html', x=x)

#class Test(db.Model):
#    id = db.Column(db.Integer, primary_key=True)