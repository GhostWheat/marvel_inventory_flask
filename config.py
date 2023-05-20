import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

# this gives access to the project in ANY OS we are in.
# allows outside files and folders to be added to the project
# base directory

load_dotenv(os.path.join(basedir, '.env'))

class Config():
    """
    This sets the Config variables for our Flask app,
    using Environment variables where available and create
    Config variables if not already there
    """
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir,'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False # this turns off messages from sqlalchemy regarding updates to our db,
                                          # otherwise gets really cluttered