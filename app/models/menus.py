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

  
    def save(self):
        # Create a New Object in DB
        if self.id is None:
            with mydb.cursor() as cursor:
                sql = "INSERT INTO menus(nombre, ruta, tipo, estatus) VALUES(%s, %s, %s, %s)"
                val = (self.nombre, self.ruta, self.tipo, self.tipo, self.estatus)
                cursor.execute(sql, val)
                mydb.commit()
                self.id = cursor.lastrowid
                return self.id 
            # Update an Object
        else:
            with mydb.cursor() as cursor:
                sql = "UPDATE menus SET nombre = %s, ruta = %s, tipo = %s, estatus %s"
                val = (self.nombre, self.ruta, self.tipo, self.estatus)
                cursor.execute(sql, val)
                mydb.commit()
                return self.id
            # Eliminar 
    def delete(self):
        with mydb.cursor() as cursor:
            sql = f"DELETE FROM menus WHERE id = { self.id }"
            cursor.execute(sql)
            mydb.commit()
            return self.id
    @staticmethod
    def get(id):
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT nombre, ruta, tipo, estatus FROM menus WHERE id  = { id }"
            cursor.execute(sql)
            result = cursor.fetchone()
            menus = Menus(result["nombre"], result["ruta"], result["tipo"], result["estatus"], id)
            return menus
        
    @staticmethod
    def get_all():
        roles = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT id, nombre, ruta, tipo,estatus FROM menus"
            cursor.execute(sql)
            result = cursor.fetchall()
            for item in result:
                print(item)
                roles.append(Menus(item["nombre"], item["ruta"], item["tipo"], item["estatus"], item["id"]))
            return roles
        
    @staticmethod
    def count_all():
        with mydb.cursor() as cursor:
            sql = f"SELECT COUNT(id) FROM menus"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result[0]
    
   
    def __str__(self):
        return f"{ self.id } - { self.nombre }"