import os


DEBUG = True
TESTING = True
JSON_AS_ASCII = False
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = False