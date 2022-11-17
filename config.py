import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

# Give access to the project from and Operating System
# WE find ourselves in
# Allow outside file/folders to be added to the project from the
# base directory

load_dotenv(os.path.join(basedir, '.env'))

class Config(): 
    """
    Set config variable for the flask app.
    Using environment variables where available
    Otherwise create the confid variable if not done already.

    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Nana nana boo boo youll never guess!'
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEPLOY_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False #turns off updates from sqlalchemy


    

