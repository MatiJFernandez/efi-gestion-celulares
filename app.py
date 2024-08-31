import os
from dotenv import load_dotenv  
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'SQLALCHEMY_DATABASE_URI'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get(
    'SECRET_KEY'
)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Equipo, Marca, Modelo, Fabricante, Proveedor, Accesorio

@app.route("/")
def index():

    return render_template("index.html")

@app.route("/celulares")
def celulares():

    return render_template("celulares.html")