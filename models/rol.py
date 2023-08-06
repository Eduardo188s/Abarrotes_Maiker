from .db import get_connection
from werkzeug.security import generate_password_hash, check_password_hash

mydb = get_connection()

class Role:

    def __init__(self, nombre,  descripcion, id = None):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion

    def save(self):
        # Create a New Object in DB
        if self.id is None:
            with mydb.cursor() as cursor:
                sql = "INSERT INTO roles(nombre, descripcion) VALUES(%s, %s)"
                val = (self.nombre,self.descripcion)
                cursor.execute(sql, val)
                mydb.commit()
                self.id = cursor.lastrowid
                return self.id
        # Update an Object
        else:
            with mydb.cursor() as cursor:
                sql = "UPDATE roles SET nombre = %s, descripcion = %s"
                val = (self.nombre, self.descripcion)
                cursor.execute(sql, val)
                mydb.commit()
                return self.id
            
    def delete(self):
        with mydb.cursor() as cursor:
            sql = f"DELETE FROM roles WHERE id = { self.id }"
            cursor.execute(sql)
            mydb.commit()
            return self.id
            
    @staticmethod
    def get(id):
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT nombre, descripcion FROM roles WHERE id  = { id }"
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)
            roles = Role(result["nombre"], result["descripcion"], id)
            return roles
        
    @staticmethod
    def get_all():
        roles = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT id, nombre, descripcion FROM roles"
            cursor.execute(sql)
            result = cursor.fetchall()
            for item in result:
                roles.append(Role(item["nombre"], item["descripcion"], item["id"]))
            return roles
    
    @staticmethod
    def count_all():
        with mydb.cursor() as cursor:
            sql = f"SELECT COUNT(id) FROM roles"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result[0]
        
    def __str__(self):
        return f"{ self.id } - { self.nombre }"