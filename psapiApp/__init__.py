from flask import Flask
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
app.config['SECRET_KEY'] = 'ThiIsAOpenSourceProject'

import psapiApp.model
import psapiApp.controller
import psapiApp.views
print('hola')
from psapiApp import * #Por qué tengo que importar todo?

if __name__ == '__main__':
    app.run(debug=True)