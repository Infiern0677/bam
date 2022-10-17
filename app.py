from flask import Flask, jsonify

from config.config import Devconfig
from routes.bam_users_r import users
from utils.db import db

app = Flask(__name__)
app.config.from_object(Devconfig)
db.init_app(app)
app.register_blueprint(users)

@app.route('/')
def index():
    return jsonify({'message': 'welcome'})

def pagina_no_encontrada(error):
    return "<h1>La pagina a la que intentas acceder no existe...</h1>"

if __name__=="__main__":
    app.register_error_handler(404 , pagina_no_encontrada)
    app.run(debug=True)