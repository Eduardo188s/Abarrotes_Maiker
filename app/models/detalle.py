from .db import get_connection

mydb = get_connection()

class   Detalle:

    def __init__(self, id_compra, id_producto, cantidad_compra,nombre_producto,sub_total, total, id=None):
        self.id = id
        self.id_compra = id_compra
        self.id_producto = id_producto
        self.cantidad_compra = cantidad_compra
        self.nombre_producto = nombre_producto
        self.sub_total = sub_total
        self.total = total

    @staticmethod
    def getAll(id_compra):        
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT c.id , c.id_producto, c.id_compra, c.cantidad_compra, p.nombre_producto, p.precio_producto FROM detalles_de_la_compra c inner join producto p on p.id_producto = c.id_producto where id_compra =  { id_compra } ;"

            detalleLista = []
            cursor.execute(sql)
            result = cursor.fetchall()
            for item in result:
                cantidad = item["cantidad_compra"]
                subtotal = item["precio_producto"] * cantidad
                total = subtotal + (subtotal * 0.16)
                detalleLista.append(
                    Detalle(id_compra = item["id_compra"], id_producto=item["id_producto"], nombre_producto=item["nombre_producto"],
                            cantidad_compra = cantidad, sub_total = subtotal, total = total))
                print(item)
            
            return detalleLista
    
    @staticmethod
    def saveOfCarrito(id_compra):
        # Create a New Object in DB
        with mydb.cursor() as cursor:
            sql = f"INSERT INTO detalles_de_la_compra(id_compra, id_producto,cantidad_compra) SELECT id_compra, id_producto, cantidad FROM carrito_productos WHERE id_compra = {id_compra};"
            cursor.execute(sql)
            mydb.commit()


    @staticmethod
    def deleteCarrito(id_compra):
        # Create a New Object in DB
        with mydb.cursor() as cursor:
            sql = f"DELETE FROM  carrito_productos WHERE id_compra = {id_compra};"
            cursor.execute(sql)
            mydb.commit()
            