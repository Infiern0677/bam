from utils.db import db


class Bam_usuarios(db.Model):
    # __abstract__ = True"""
    id_usuario = db.Column(db.Integer, primary_key=True, nullable=True)
    nombres_u = db.Column(db.String(20), nullable=False)
    apellidos_u = db.Column(db.String(20), nullable=False)
    tipo_docuemento = db.Column(db.Integer, index=True, nullable=False)
    rol = db.Column(db.Integer, index=True, nullable=False)
    sexo_u = db.Column(db.Integer, index=True, nullable=False)
    documento = db.Column(db.String(11), unique=True, nullable=False)
    user = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    direccion = db.Column(db.String(50), nullable=False)
    fecha = db.Column(db.TIMESTAMP)
    estado = db.Column(db.Integer, nullable=False, default=1)
    
    
    def __init__(self, nombres_u, apellidos_u, tipo_docuemento, rol, sexo_u, documento, user, password, email, phone, direccion):
        self.nombres_u = nombres_u
        self.apellidos_u = apellidos_u
        self.tipo_docuemento = tipo_docuemento
        self.rol = rol
        self.sexo_u = sexo_u
        self.documento = documento
        self.user = user
        self.password = password
        self.email = email
        self.phone = phone
        self.direccion = direccion
        self.estado = 1
  

    def getDatos(self):
        return {
            'id_usuario': self.id_usuario,
            'nombres_u': self.nombres_u,
            'apellidos_u': self.apellidos_u,
            'tipo_docuemento': self.tipo_docuemento,
            'rol': self.rol,
            'sexo_u': self.sexo_u,
            'documento': self.documento,
            'user': self.user,
            'password': self.password,
            'email': self.email,
            'phone': self.phone,
            'direccion': self.direccion,
            'fecha': self.fecha,
            'estado': self.estado

        }