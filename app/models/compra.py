from .db import get_connection

import uuid
mydb = get_connection()

class   Compra:

    def __init__(self, fecha_compra, ticket = None, total_compra = '', id_compra=None):
        self.id_compra = id_compra
        self.fecha_compra = fecha_compra
        self.ticket = ticket
        self.total_compra = total_compra

    def save(self):
        # Create a New Object in DB
        ticket = uuid.uuid4()
        if self.id_compra is None:
            with mydb.cursor() as cursor:
                sql = "INSERT INTO compra(fecha_compra, ticket) VALUES(%s, %s)"
                val = (self.fecha_compra, str( ticket))
                print("producto")
                print(str(ticket))
                cursor.execute(sql, val)
                mydb.commit()
                self.id_compra = cursor.lastrowid
                return self.id_compra
        # Update an Object
        else:
            with mydb.cursor() as cursor:
                sql = "UPDATE compra SET fecha_compra =%s, WHERE id_compra = %s"
                val = (self.fecha_compra)
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
            sql = f"SELECT id_compra, fecha_compra FROM compra WHERE id_compra = { id_compra }"
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)
            compra = Compra(result["fecha_compra"], id_compra = id_compra)
            return compra
        
    @staticmethod
    def get_all():
        compra = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT fecha_compra,ticket, id_compra, total_compra FROM compra ORDER BY id_compra DESC"
            cursor.execute(sql)
            result = cursor.fetchall()
            for item in result:
                compra.append(Compra(fecha_compra=item["fecha_compra"], ticket=item["ticket"],id_compra= item["id_compra"], total_compra=item['total_compra']))
                print(item)
            return compra
    
    @staticmethod
    def count_all():
        with mydb.cursor() as cursor:
            sql = f"SELECT COUNT(id_compra) FROM compra"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result[0]
    
    @staticmethod
    def get_status(id_compra):
        # Create a New Object in DB
        with mydb.cursor() as cursor:
            sql = f"SELECT status FROM compra WHERE id_compra = {id_compra};"
            cursor.execute(sql)
            result =cursor.fetchone()
            return result[0]
        
    @staticmethod
    def save_status(id_compra, status):
            with mydb.cursor() as cursor:
                sql = "UPDATE compra SET status =%s WHERE id_compra = %s"
                val = (status, id_compra)
                cursor.execute(sql, val)
                mydb.commit()
                return id_compra
        
    def __str__(self):
        return f"{ self.id_compra } - { self.ticket }"