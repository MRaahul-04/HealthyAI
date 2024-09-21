# config.py

# import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/healthyai_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False