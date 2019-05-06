How to build a Flask Web App with SQLAlquemy on PythonAny

* Diagram (Larger Application Concepts)

psapiApp/
    psapi/ (venv)
    psapiApp.egg-info
    psapiApp/
    Helper/
        AlquemyEncoder.py (Class that parsed to JSON SQLAlquemy return objects)
    static/
    templates/
        allAccountsApi.html
        index.html
    __init__.py
    setup.py
    config.cfg
    views.py
    model.py 
    controller.py
    Readme
    requirements.txt

* PythonAnyWhere allow access to externals DataBases only with paid Accounts.
https://help.pythonanywhere.com/pages/AccessingMySQLFromOutsidePythonAnywhere/
    
* Create DB with mySQL on pythonanywhere

https://help.pythonanywhere.com/pages/UsingMySQL/

Create a new file called DATABASE.cfg into de app folder: 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '<your_username>$<your_database_name>',
        'USER': '<your_username>',
        'PASSWORD': '<your_mysql_password>',
        'HOST': '<your_mysql_hostname>',
    }
}

Then:
    1. Open __init__.py file
    2. Modify app.config.from_pyfile() to Modify app.config.from_pyfile('DATABASE.cfg')

    Note: If you save DATABASE.cfg in another folder you have to especified the path/
