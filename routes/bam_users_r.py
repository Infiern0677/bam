from flask import Blueprint

from controllers import bam_users_c
from models.Bam_user import *

users = Blueprint('users', __name__)



@users.route('/usuarios', methods=['GET','POST'])
def usuarios():
    return bam_users_c.usuarios()

@users.route('/usuarios/<id_usuario>')
def usuario(id_usuario):
    #usuario = Usuarios.query.filter_by(idUsuario=idUsuario).first()
    return bam_users_c.usuario(id_usuario)

@users.route('/usuarios/editar/<id_usuario>', methods=['PUT'])
def editarUsuario(id_usuario):
    return bam_users_c.editarUsuario(id_usuario)

@users.route('/usuarios/eliminar/<id_usuario>', methods=['DELETE'])
def eliminarUsuario(id_usuario):
    return bam_users_c.eliminarUsuario(id_usuario)
    