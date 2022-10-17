from os import environ, getcwd, path

from dotenv import load_dotenv

basedir = path.dirname(getcwd())

load_dotenv(path.join(basedir, ".env"))

class config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = environ.get("SECRET_KEY")
    FLASK_ENV = environ.get("FLASK_ENV")


class Devconfig(config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost/bam_bd'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    
    
