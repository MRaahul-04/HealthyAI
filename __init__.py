# __init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
import pymysql

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize SQLAlchemy
db = SQLAlchemy(app)

pymysql.install_as_MySQLdb()

# Import routes after app and db initialization to avoid circular imports
# from routes import *

if __name__ == "__main__":
    app.run(debug=True, port=5000)