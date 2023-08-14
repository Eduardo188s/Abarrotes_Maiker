from .db import get_connection
from models.compra import Compra

import datetime
mydb = get_connection()

class Carrito:

    def __init__(self, id_producto, cantidad, nombre_producto=None, sub_total=None, total=None, id_compra=None, id=None):
        self.id = id
        self.id_compra = id_compra        
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.nombre_producto = nombre_producto
        self.sub_total = sub_total
        self.total = total

    def save(self):
        # Create a New Object in DB
        if self.id is None:
            fecha_compra=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            print(self.id_compra)
            if self.id_compra != None:
                compra = Compra.get(self.id_compra)
            else:
                print("Se crea la compra")
                compra = Compra(fecha_compra)            
                compra.save()
            with mydb.cursor() as cursor:
                sql = "INSERT INTO carrito_productos(id_producto, id_compra, cantidad) VALUES(%s, %s, %s)"
                val = (self.id_producto, compra.id_compra, self.cantidad)
                cursor.execute(sql, val)
                mydb.commit()
                self.id = cursor.lastrowid
                return self.id
        # Update an Object
        else:
            with mydb.cursor() as cursor:
                sql = "UPDATE carrito_compra SET id_producto = %s, id_compra = %s, cantidad = %s WHERE id = %s"
                val = (self.id_producto, self.id_compra, self.cantidad, self.id)
                cursor.execute(sql, val)
                mydb.commit()
                return self.id
            
    def delete(self):
        with mydb.cursor() as cursor:
            sql = f"DELETE FROM carrito_productos WHERE id = { self.id }"
            cursor.execute(sql)
            mydb.commit()
            return self.id
            
    @staticmethod
    def get(id):
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT id_producto, id_compra, cantidad FROM carrito_productos WHERE id = { id }"
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)
            carrito_productos = Carrito(result["id_producto"], result["id_compra"], result["cantidad"], id)
            return carrito_productos
        
    @staticmethod
    def get_all(id_compra):
        carrito_productos = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT c.id , c.id_producto, c.id_compra, c.cantidad, p.nombre_producto, p.precio_producto FROM carrito_productos c inner join producto p on p.id_producto = c.id_producto where id_compra =  { id_compra } ;"
            cursor.execute(sql)
            result = cursor.fetchall()
            for item in result:
                cantidad = item["cantidad"]
                subtotal = item["precio_producto"] * cantidad
                total = subtotal + (subtotal * 0.16)
                carrito_productos.append(Carrito(item["id_producto"], item["cantidad"],item["nombre_producto"], subtotal, total, item["id_compra"], item["id"]))
            return carrito_productos
    
    @staticmethod
    def count_all():
        with mydb.cursor() as cursor:
            sql = f"SELECT COUNT(id) FROM carrito_productos"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result[0]
        
    def __str__(self):
        return f"{ self.id } - { self.id_producto }"