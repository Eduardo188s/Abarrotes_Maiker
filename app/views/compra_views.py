from flask import Blueprint, render_template, request, redirect, flash, url_for, session
from models.compra import Compra
from forms.compra_forms import CreateCompraForm, UpdateCompraForm
from decorators import login_required
from models.menu_roles import Menu_roles
from models.carrito import Carrito
from models.detalle import Detalle


compra_views=Blueprint('compra',__name__)
@compra_views.route('/compra/')
@ login_required
def compra():

    nav = Menu_roles.get(session.get("role"))
    #Consultas categorias de DB
    compras = Compra.get_all()
   
    return render_template('compra/compra.html', nav = nav, compra=compras)

@compra_views.route('/compra/create/', methods=('GET', 'POST'))
def create_com():
    nav = Menu_roles.get(session.get("role"))
    form=CreateCompraForm()
    print(request.args.__len__)
    carritoCompras = []
    
    id_compra = None

    if request.args.__len__() > 0:
        id_compra = request.args["id_compra"]
        if id_compra:
            carritoCompras = Carrito.get_all(id_compra)
    
    if form.validate_on_submit():
            
        id_producto = form.producto.data
        cantidad = form.cantidad_compra.data

        carrito = Carrito(id_producto, cantidad, id_compra = id_compra)
        carrito.save()
       
        return render_template('compra/create_com.html', form=form, nav = nav, carritoCompras = carritoCompras,id_compra= id_compra)
    return render_template('compra/create_com.html', form=form, nav = nav, carritoCompras = carritoCompras,id_compra= id_compra)


@compra_views.route('/compra/<int:id_compra>/update/', methods=('GET', 'POST'))
def update_com(id_compra):
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
    return render_template('compra/create_com.html', form=form)

@compra_views.route('/compra/<int:id_compra>/delete/', methods=('POST', 'DELETE'))
def delete_com(id_compra):
    com=Compra.get(id_compra)
    com.delete()
    return redirect(url_for('compra.compra'))


@compra_views.route('/compra/ticket/', methods=("GET", "POST"))
def get_ticket():
    nav = Menu_roles.get(session.get("role"))
    listaTicket = []

    if request.args.__len__() > 0:
        id_compra = request.args["id_compra"]
        if id_compra:
            listaTicket = Detalle.getAll(id_compra)

            subtotal = 0
            total = 0

            for item in listaTicket:
                subtotal += item.sub_total
                total += item.total
                
              
            

        return render_template('compra/ticket.html',  nav = nav, listaTicket = listaTicket,total = total, sub_total = subtotal)
    return render_template('compra/ticket.html',nav = nav, listaTicket = listaTicket)
