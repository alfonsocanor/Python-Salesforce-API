#from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from psapiApp import app

db = SQLAlchemy(app)
print(app.name)
print(db)

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)

class Account(db.Model):
    dni = db.Column(db.String(8), primary_key=True)
    Nombre = db.Column(db.String(20))
    Apellido = db.Column(db.String(20))
    email = db.Column(db.String(60), unique=True)

db.create_all()

class CRUMAccount():
    def insertAccount(self, setDni, setNombre, setApellido, setEmail):
        acc = Account(dni=setDni, Nombre=setNombre, Apellido=setApellido, email=setEmail)
        db.session.add(acc)
        db.session.commit()

class CRUMTest():
    #admin = Test(id='1')
    #db.session.add(admin)
    #db.session.commit()
    def insertTest(self, newId):
        newTest = Test(id=newId)
        db.session.add(newTest)
        db.session.commit()