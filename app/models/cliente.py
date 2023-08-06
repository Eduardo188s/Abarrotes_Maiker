from .db import get_connection

mydb = get_connection()

class Cliente:

    def __init__(self, nombre, a_paterno, a_materno, domicilio, id_cliente=None):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.a_paterno = a_paterno
        self.a_materno = a_materno
        self.domicilio = domicilio

    def save(self):
        # Create a New Object in DB
        if self.id_cliente is None:
            with mydb.cursor() as cursor:
                sql = "INSERT INTO cliente(nombre, a_paterno, a_materno, domicilio) VALUES(%s, %s, %s, %s)"
                val = (self.nombre, self.a_paterno, self.a_materno, self.domicilio)
                cursor.execute(sql, val)
                mydb.commit()
                self.id_cliente = cursor.lastrowid
                return self.id_cliente
        # Update an Object
        else:
            with mydb.cursor() as cursor:
                sql = "UPDATE cliente SET nombre = %s, a_paterno = %s, a_materno = %s, domicilio = %s WHERE id_cliente = %s"
                val = (self.nombre, self.a_paterno, self.a_materno, self.domicilio, self.id_cliente)
                cursor.execute(sql, val)
                mydb.commit()
                return self.id_cliente
            
    def delete(self):
        with mydb.cursor() as cursor:
            sql = f"DELETE FROM cliente WHERE id_cliente = { self.id_cliente }"
            cursor.execute(sql)
            mydb.commit()
            return self.id_cliente
            
    @staticmethod
    def get(id_cliente):
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT nombre, a_paterno, a_materno, domicilio FROM cliente WHERE id_cliente = { id_cliente }"
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)
            cliente = Cliente(result["nombre"], result["a_paterno"], result["a_materno"], result["domicilio"], id_cliente)
            return cliente
        
    @staticmethod
    def get_all():
        cliente = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT id_cliente, nombre, a_paterno, a_materno, domicilio FROM cliente"
            cursor.execute(sql)
            result = cursor.fetchall()
            for item in result:
                cliente.append(Cliente(item["nombre"], item["a_paterno"], item["a_materno"], item["domicilio"], item["id_cliente"]))
            return cliente
    
    @staticmethod
    def count_all():
        with mydb.cursor() as cursor:
            sql = f"SELECT COUNT(id_cliente) FROM cliente"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result[0]
        
    def __str__(self):
        return f"{ self.id_cliente } - { self.nombre }"