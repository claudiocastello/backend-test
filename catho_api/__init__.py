from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_whooshee import Whooshee


app = Flask(__name__)
app.config.from_pyfile('config.py')

## SQLAlchemy ##
db = SQLAlchemy(app)

## Whoshee
whooshee = Whooshee(app)

import catho_api.views
