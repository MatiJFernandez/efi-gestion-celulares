import os
from dotenv import load_dotenv  
from flask import Flask, render_template, request, redirect, url_for
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

@app.route("/marcaList", methods = ['POST', 'GET'])
def marcas():
    marcas = Marca.query.all()

    if request.method == 'POST':
        nombre = request.form['nombre']
        nuevaMarca = Marca(nombre = nombre)
        db.session.add(nuevaMarca)
        db.session.commit()
        return redirect(url_for('marcas'))

    return render_template("marcaList.html", marcasFront = marcas)

@app.route("/modeloList", methods = ['POST', 'GET'])
def modelos():
    modelos = Modelo.query.all()

    if request.method == 'POST':
        nombre = request.form['nombre']
        nuevoModelo = Modelo(nombre = nombre)
        db.session.add(nuevoModelo)
        db.session.commit()
        return redirect(url_for('modelos'))
    
    return render_template("modeloList.html", modelosFront = modelos)

@app.route("/fabricanteList", methods = ['POST', 'GET'])
def fabricantes():
    fabricantes = Fabricante.query.all()

    if request.method == 'POST':
        nombre = request.form['nombre']
        nuevoFabricante = Fabricante(nombre = nombre)
        db.session.add(nuevoFabricante)
        db.session.commit()
        return redirect(url_for('fabricantes'))
    
    return render_template("fabricanteList.html", fabricantesFront = fabricantes)

@app.route("/proveedorList", methods = ['POST', 'GET'])
def proveedores():
    proveedores = Proveedor.query.all()

    if request.method == 'POST':
        nombre = request.form['nombre']
        nuevoProveedor = Proveedor(nombre = nombre)
        db.session.add(nuevoProveedor)
        db.session.commit()
        return redirect(url_for('proveedores'))
    
    return render_template("proveedorList.html", proveedoresFront = proveedores)

@app.route("/accesorioList", methods = ['POST', 'GET'])
def accesorios():
    accesorios = Accesorio.query.all()

    if request.method == 'POST':
        nombre = request.form['nombre']
        nuevoAccesorio = Accesorio(nombre = nombre)
        db.session.add(nuevoAccesorio)
        db.session.commit()
        return redirect(url_for('accesorios'))
    
    return render_template("accesorioList.html", accesoriosFront = accesorios)