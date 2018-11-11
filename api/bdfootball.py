import flask
import json
from flask import request, jsonify
import mysql.connector

# Creación de una nueva aplicación web
app = flask.Flask(__name__)

# Conexión al SGBD
conn = mysql.connector.connect(user="root",host="localhost",password="root")
cursor = conn.cursor()
cursor.execute("USE football")

# Definición de las rutas
@app.route('/', methods=['GET'])
def home():
    return '''<h1>API football</h1>
<p>Un prototipo de API para la base de datos football.</p>'''

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>No se pudo encontrar el recurso.</p>", 404

@app.route('/api_football/v1/resources/jugadores/all', methods=['GET'])
def api_users_all():
    result=cursor.execute('SELECT * FROM player;')
    all_films =cursor.fetchall()
    row_headers=[x[0] for x in cursor.description]
    json_data=[]
    for result in all_films:
        json_data.append(dict(zip(row_headers,result)))
    return jsonify(json_data)

@app.route('/api_valdivia/v1/resources/jugadores/turkey', methods=['GET'])
def api_camiones_all():
    result=cursor.execute('SELECT * FROM player WHERE country="Turkey"')
    all_films =cursor.fetchall()
    row_headers=[x[0] for x in cursor.description]
    json_data=[]
    for result in all_films:
        json_data.append(dict(zip(row_headers,result)))
    return jsonify(json_data)






app.run(debug=False,port=1234)
