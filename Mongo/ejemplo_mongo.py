import pymongo
from pymongo import MongoClient

#Nos conectamos a la instancia de Mongo local, puerto 27017
client = MongoClient('localhost', 27017)

#Nos conectamos a la BD 'notebook5_db'
db = client['notebook5_db']

#Dentro de la BD, creamos una nueva colección llamada 'personas'
collection = db['personas']

aDocument = {"Nombre":"Juan", "Edad":23, "Asignaturas":["INFO261", "INFO267", "INFO268"] }
otherDocument = {"Nombre":"Maria", "Edad":24, "Asignaturas":["INFO261", "INFO267", "INFO268", "INFO331"] }

collection.insert_many([aDocument,otherDocument])
