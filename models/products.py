from .db import get_connection

mydb = get_connection()

class Product:

    def __init__(self, nombre_producto, marca_producto, cb_producto, precio_producto, id_producto=None):
        self.id_producto = id_producto
        self.nombre_producto = nombre_producto
        self.marca_producto = marca_producto
        self.cb_producto = cb_producto
        self.precio_producto = precio_producto

    def save(self):
        # Create a New Object in DB
        if self.id_producto is None:
            with mydb.cursor() as cursor:
                sql = "INSERT INTO producto(nombre_producto, marca_producto, cb_producto, precio_producto) VALUES(%s, %s, %s, %s)"
                val = (self.nombre_producto, self.marca_producto, self.cb_producto, self.precio_producto)
                cursor.execute(sql, val)
                mydb.commit()
                self.id_producto = cursor.lastrowid
                return self.id_producto
        # Update an Object
        else:
            with mydb.cursor() as cursor:
                sql = "UPDATE producto SET nombre_producto = %s, marca_producto = %s, cb_producto = %s, precio_producto = %s WHERE id_producto = %s"
                val = (self.nombre_producto, self.marca_producto, self.cb_producto, self.precio_producto, self.id_producto)
                cursor.execute(sql, val)
                mydb.commit()
                return self.id_producto
            
    def delete(self):
        with mydb.cursor() as cursor:
            sql = f"DELETE FROM producto WHERE id_producto = { self.id_producto }"
            cursor.execute(sql)
            mydb.commit()
            return self.id_producto
            
    @staticmethod
    def get(id_producto):
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT nombre_producto, marca_producto, cb_producto, precio_producto FROM producto WHERE id_producto = { id }"
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)
            producto = Product(result["nombre_producto"], result["marca_producto"], result["cb_producto"], result["precio_producto"], id)
            return producto
        
    @staticmethod
    def get_all():
        producto = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT id_producto, nombre_producto, marca_producto, cb_producto, precio_producto FROM producto"
            cursor.execute(sql)
            result = cursor.fetchall()
            for item in result:
                producto.append(Product(item["nombre_producto"], item["marca_producto"], item["cb_producto"], item["precio_producto"], item["id_producto"]))
            return producto
    
    @staticmethod
    def count_all():
        with mydb.cursor() as cursor:
            sql = f"SELECT COUNT(id_producto) FROM producto"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result[0]
        
    def __str__(self):
        return f"{ self.id_producto } - { self.nombre_producto }"