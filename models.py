from app import db

class Equipo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    costo = db.Column(db.Integer)  

class Marca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

    def __str__(self) -> str:
        return self.nombre

class Modelo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

    def __str__(self) -> str:
        return self.nombre

class Fabricante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

    def __str__(self) -> str:
        return self.nombre

class Proveedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

    def __str__(self) -> str:
        return self.nombre

class Accesorio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

    def __str__(self) -> str:
        return self.nombre
