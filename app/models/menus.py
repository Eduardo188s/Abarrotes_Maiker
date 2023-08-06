from .db import get_connection
from werkzeug.security import generate_password_hash, check_password_hash

mydb = get_connection()

class Menus:

    def __init__(self, nombre,  ruta, tipo, estatus, id = None):
        self.id = id
        self.nombre = nombre
        self.ruta = ruta
        self.tipo = tipo
        self.estatus = estatus

  
        
    @staticmethod
    def get_all():
        roles = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT id, nombre, ruta, tipo,estatus FROM menus"
            cursor.execute(sql)
            result = cursor.fetchall()
            for item in result:
                roles.append(Menus(item["nombre"], item["ruta"], item["tipo"], item["estatus"], item["id"]))
            return roles
    
   
    def __str__(self):
        return f"{ self.id } - { self.nombre }"