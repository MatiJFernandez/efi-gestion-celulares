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

@app.route("/marcaList")
def marcas():

    return render_template("marcaList.html")

@app.route("/modeloList")
def modelos():

    return render_template("modeloList.html")

@app.route("/fabricanteList")
def fabricantes():

    return render_template("fabricanteList.html")

@app.route("/proveedorList")
def proveedores():

    return render_template("proveedorList.html")

@app.route("/accesorioList")
def accesorios():

    return render_template("accesorioList.html")