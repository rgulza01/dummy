from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

#It can't find os.getenv("SECRET_KEY") 
app.config['SECRET_KEY'] = 'none'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://radiagulzan@db-relationship-practice-mysql:Password123!@db-relationship-practice-mysql.mysql.database.azure.com:3306/project_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from application import routes
