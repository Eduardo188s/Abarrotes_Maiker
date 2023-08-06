from .db import get_connection
from werkzeug.security import generate_password_hash, check_password_hash

mydb = get_connection()

class Menu_roles:

    def __init__(self, id, ruta,  nombre):
        self.id = id
        self.ruta = ruta
        self.nombre = nombre

    def save(self):
        # Create a New Object in DB
        if self.id is None:
            with mydb.cursor() as cursor:
                sql = "INSERT INTO menu_roles(id_rol, id_menu) VALUES(%s, %s)"
                val = (self.id_rol,self.id_mennu)
                cursor.execute(sql, val)
                mydb.commit()
                self.id = cursor.lastrowid
                return self.id
        # Update an Object
        else:
            with mydb.cursor() as cursor:
                sql = "UPDATE menu_roles SET id_rol = %s, id_menu = %s"
                val = (self.id_rol, self.id_menu)
                cursor.execute(sql, val)
                mydb.commit()
                return self.id
            
    def delete(self):
        with mydb.cursor() as cursor:
            sql = f"DELETE FROM menu_roles WHERE id = { self.id }"
            cursor.execute(sql)
            mydb.commit()
            return self.id
            
    @staticmethod
    def get(id_rol):
        menu_roles = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT m.id, m.ruta, m.nombre FROM `menu_roles` mr inner join menus m on mr.id_menu = m.id WHERE id_rol in ({id_rol},3)"
            cursor.execute(sql)
            result = cursor.fetchall()
            for item in result:
                print(item)

                menu_roles.append(Menu_roles(item["id"], item["ruta"], item["nombre"]))           
            return menu_roles
        
    @staticmethod
    def get_all():
        menu_roles = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT id, id_rol, id_menu FROM menu_roles"
            cursor.execute(sql)
            result = cursor.fetchall()
            for item in result:
                menu_roles.append(Menu_roles(item["id_rol"], item["id_menu"], item["id"]))
            return menu_roles
    
    @staticmethod
    def count_all():
        with mydb.cursor() as cursor:
            sql = f"SELECT COUNT(id) FROM menu_roles"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result[0]
        
    def __str__(self):
        return f"{ self.id } - { self.id_rol }"