from .db import get_connection

mydb = get_connection()

class Compra:

    def __init__(self, id_ticket, id_cliente, id_producto, fecha_compra, total_compra, id_compra=None):
        self.id_compra = id_compra
        self.id_ticket = id_ticket
        self.id_cliente = id_cliente
        self.id_producto = id_producto
        self.fecha_compra = fecha_compra
        self.total_compra = total_compra

    def save(self):
        # Create a New Object in DB
        if self.id_compra is None:
            with mydb.cursor() as cursor:
                sql = "INSERT INTO compra(id_ticket, id_cliente, id_producto, fecha_compra, total_compra) VALUES(%s, %s, %s, %s, %s, %s)"
                val = (self.id_ticket, self.id_cliente, self.id_producto, self.fecha_compra, self.total_compra)
                cursor.execute(sql, val)
                mydb.commit()
                self.id_compra = cursor.lastrowid
                return self.id_compra
        # Update an Object
        else:
            with mydb.cursor() as cursor:
                sql = "UPDATE compra SET id_ticket = %s, id_cliente = %s, id_producto = %s, fecha_compra =%s, total_compra = %s, WHERE id_compra = %s"
                val = (self.id_ticket, self.id_cliente, self.id_producto, self.fecha_compra, self.total_compra)
                cursor.execute(sql, val)
                mydb.commit()
                return self.id_compra
            
    def delete(self):
        with mydb.cursor() as cursor:
            sql = f"DELETE FROM compra WHERE id_compra = { self.id_compra }"
            cursor.execute(sql)
            mydb.commit()
            return self.id_compra
            
    @staticmethod
    def get(id_compra):
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT id_ticket, id_cliente, id_producto, fecha_compra, total_compra FROM compra WHERE id_compra = { id_compra }"
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)
            cliente = Cliente(result["id_ticket"], result["id_cliente"], result["id_producto"], result["fecha_compra"], result["total_compra"], id_compra)
            return cliente
        
    @staticmethod
    def get_all():
        compra = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT id_ticket, id_cliente, id_producto, fecha_compra, total_compra FROM compra"
            cursor.execute(sql)
            result = cursor.fetchall()
            for item in result:
                compra.append(Compra(item["id_ticket"], item["id_clinte"], item["id_producto"], item["fecha_Compra"], item["total_Compra"], item["id_compra"]))
            return compra
    
    @staticmethod
    def count_all():
        with mydb.cursor() as cursor:
            sql = f"SELECT COUNT(id_compra) FROM compra"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result[0]
        
    def __str__(self):
        return f"{ self.id_compra } - { self.id_ticket }"