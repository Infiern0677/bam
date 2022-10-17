from flask import jsonify, request

from models.Bam_user import *


def usuarios():
    if request.method == 'GET':
        usuarios = Bam_usuarios.query.all()
        if not usuarios:
            return jsonify({'message': 'no hay usuarios'})
        else:
            toUsers = [usuario.getDatos() for usuario in usuarios]
            return jsonify(toUsers)
    elif request.method == 'POST':
        nombres_u = request.json["nombres_u"]
        apellidos_u =  request.json["apellidos_u"]
        tipo_docuemento = request.json["tipo_docuemento"]
        rol =  request.json["rol"]
        sexo_u =  request.json["sexo_u"]
        documento = request.json["documento"]
        user =  request.json["user"]
        password = request.json["password"]
        email = request.json["email"]
        phone = request.json["phone"]
        direccion = request.json["direccion"]
        new_usuario = Bam_usuarios(nombres_u,apellidos_u,tipo_docuemento,rol,sexo_u,documento,user,password,email,phone,direccion)
        db.session.add(new_usuario)
        db.session.commit()
        return jsonify({'message':'usuario guardado con exito'})

def usuario(id_usuario):
    #usuario = Usuarios.query.filter_by(idUsuario=idUsuario).first()
    usuario = Bam_usuarios.query.get(id_usuario)
    if not usuario:
        return jsonify({'message': 'Usuario not found'})
    else:
        return jsonify(usuario.getDatos())

def editarUsuario(id_usuario):
    usuario = Bam_usuarios.query.get(id_usuario)
    if not usuario:
        return jsonify({'message': 'Usuario not found'})
    else:
        usuario.nombres_u = request.json["nombres_u"]
        usuario.apellidos_u =  request.json["apellidos_u"]
        usuario.tipo_docuemento = request.json["tipo_docuemento"]
        usuario.rol =  request.json["rol"]
        usuario.sexo_u =  request.json["sexo_u"]
        usuario.documento = request.json["documento"]
        usuario.user =  request.json["user"]
        usuario.password = request.json["password"]
        usuario.email = request.json["email"]
        usuario.phone = request.json["phone"]
        usuario.direccion = request.json["direccion"]
        db.session.commit()
        return jsonify({'message': 'Usuario actualizado con exito'})

def eliminarUsuario(id_usuario):
    usuario = Bam_usuarios.query.get(id_usuario)
    if not usuario:
        return jsonify({'message': 'Usuario not found'})
    else:
        db.session.delete(usuario)
        db.session.commit()
        return jsonify({'message': 'Usuario eliminado con exito'})