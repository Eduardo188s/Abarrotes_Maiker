from flask import Blueprint, render_template, request, redirect, flash, url_for, session
from models.compra import Compra
from forms.compra_forms import CreateCompraForm, UpdateCompraForm
from decorators import login_required
from models.menu_roles import Menu_roles
from models.carrito import Carrito
from models.detalle import Detalle
import datetime

compra_views=Blueprint('compra',__name__)
@compra_views.route('/compra/')
@ login_required
def compra():

    nav = Menu_roles.get(session.get("role"))
    #Consultas categorias de DB
    compras = Compra.get_all()
   
    return render_template('compra/compra.html', nav = nav, compra=compras)


@compra_views.route('/compra/create/<int:id_compra>', methods=('GET','POST'))
@compra_views.route('/compra/create/', defaults={'id_compra': None}, methods=('GET','POST'))
@ login_required
def create_com(id_compra):
    nav = Menu_roles.get(session.get("role"))
    form=CreateCompraForm()
    print(request.args.__len__)
    carritoCompras = []
    id_compra =id_compra if id_compra is not None else 0
    carritoCompras = Carrito.get_all(id_compra)
   
    if request.method == 'POST' and form.validate_on_submit():
        if id_compra== 0:
            new_compra = Compra(fecha_compra=datetime.datetime.now())
            id_compra = new_compra.save()
            
        id_producto = form.producto.data
        cantidad = form.cantidad_compra.data
        carrito = Carrito(id_producto, cantidad, id_compra = id_compra)
        carrito.save()
        print(carritoCompras)
        return redirect(url_for('compra.create_com',id_compra=id_compra))
    return render_template(f'compra/create_com.html', form=form, nav = nav, carritoCompras = carritoCompras,id_compra= id_compra)

@compra_views.route('/compra/<int:id_producto>/update/', methods=('GET', 'POST'))
@ login_required
def update_com(id_compra):
    nav = Menu_roles.get(session.get("role"))
    form=UpdateCompraForm()
    com=Compra.get(id_compra)
    if form.validate_on_submit():
        com.fecha_compra = form.fecha_compra.data
        com.cantidad_compra = form.cantidad_compra.data
        com.total_compra = form.total_compra.data
        com.save()
        return redirect(url_for('compra.compra'))
    form.fecha_compra.data = com.fecha_compra
    form.cantidad_compra.data = com.cantidad_compra
    form.total_compra.data = com.total_compra
    return render_template('compra/create_com.html', form=form, nav = nav)

@compra_views.route('/compra/<int:id_compra>/<int:id_producto>/delete/', methods=('POST',))
def delete_com(id_compra, id_producto):
    car=Carrito.get_item(id_compra, id_producto)
    print(id_compra, id_producto)
    print(car)
    car.delete()
    return redirect(url_for('compra.create_com', id_compra = id_compra))


@compra_views.route('/compra/ticket/<int:id_compra>', methods=("GET", "POST"))
@ login_required
def get_ticket(id_compra):
    nav = Menu_roles.get(session.get("role"))
    listaTicket = []
    print("Recibiendo Ticket")
    # if request.args.__len__() > 0:
    # id_compra = request.args["id_compra"]
    print(id_compra)
    if id_compra:

        status_compra = Compra.get_status(id_compra)
        if status_compra is None:
            Compra.save_status(id_compra, "F")

            Detalle.saveOfCarrito(id_compra)
        listaTicket = Detalle.getAll(id_compra)

        subtotal = 0
        total = 0
        
        for item in listaTicket:
            subtotal += item.sub_total
            total += item.total
                
        return render_template('compra/ticket.html',  nav = nav, listaTicket = listaTicket,total = total, sub_total = subtotal)
    return render_template('compra/ticket.html',nav = nav, listaTicket = listaTicket)