from .db import get_connection

mydb = get_connection()

class Proveedor:

    def __init__(self, nombre_proveedor, a_paterno, a_materno, marca_proveedor, direccion_proveedor, correo_proveedor, telefono_proveedor, id_proveedor=None):
        self.id_proveedor = id_proveedor
        self.nombre_proveedor = nombre_proveedor
        self.a_paterno = a_paterno
        self.a_materno = a_materno
        self.marca_proveedor = marca_proveedor
        self.direccion_proveedor = direccion_proveedor
        self.correo_proveedor = correo_proveedor
        self.telefono_proveedor = telefono_proveedor

    def save(self):
        # Create a New Object in DB
        if self.id_proveedor is None:
            with mydb.cursor() as cursor:
                sql = "INSERT INTO proveedor(nombre_proveedor, a_paterno, a_materno, marca_proveedor, direccion_proveedor, correo_proveedor, telefono_proveedor) VALUES(%s, %s, %s, %s, %s, %s, %s)"
                val = (self.nombre_proveedor,self.a_paterno, self.a_materno, self.marca_proveedor, self.direccion_proveedor, self.correo_proveedor, self.telefono_proveedor)
                cursor.execute(sql, val)
                mydb.commit()
                self.id_proveedor = cursor.lastrowid
                return self.id_proveedor
        # Update an Object
        else:
            with mydb.cursor() as cursor:
                sql = "UPDATE proveedor SET nombre_proveedor = %s, a_paterno = %s, a_materno = %s, marca_proveedor = %s, direccion_proveedor = %s, correo_proveedor = %s, telefono_proveedor = %s WHERE id_proveedor = %s"
                val = (self.nombre_proveedor, self.a_paterno, self.a_materno,  self.marca_proveedor, self.direccion_proveedor, self.correo_proveedor, self.telefono_proveedor, self.id_proveedor)
                cursor.execute(sql, val)
                mydb.commit()
                return self.id_proveedor
            
    def delete(self):
        with mydb.cursor() as cursor:
            sql = f"DELETE FROM proveedor WHERE id_proveedor = { self.id_proveedor }"
            cursor.execute(sql)
            mydb.commit()
            return self.id_proveedor
            
    @staticmethod
    def get(id_proveedor):
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT nombre_proveedor, a_paterno, a_materno, marca_proveedor, direccion_proveedor, correo_proveedor, telefono_proveedor FROM proveedor WHERE id_proveedor = { id_proveedor }"
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)
            proveedor = Proveedor(result["nombre_proveedor"], result["a_paterno"], result["a_materno"], result["marca_proveedor"], result["direccion_proveedor"], result["correo_proveedor"], result["telefono_proveedor"], id_proveedor)
            return proveedor
        
    @staticmethod
    def get_all():
        proveedor = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT id_proveedor, nombre_proveedor, a_paterno, a_materno, marca_proveedor, direccion_proveedor, correo_proveedor, telefono_proveedor FROM proveedor"
            cursor.execute(sql)
            result = cursor.fetchall()
            for item in result:
                proveedor.append(Proveedor(item["nombre_proveedor"], item["a_paterno"], item["a_materno"], item["marca_proveedor"], item["direccion_proveedor"], item["correo_proveedor"], item["telefono_proveedor"], item["id_proveedor"]))
            return proveedor
    
    @staticmethod
    def count_all():
        with mydb.cursor() as cursor:
            sql = f"SELECT COUNT(id_proveedor) FROM proveedor"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result[0]
        
    def __str__(self):
        return f"{ self.id_proveedor } - { self.nombre_proveedor }"