from flask import Blueprint, render_template, request, redirect, flash, url_for, session
from models.compra import Compra
from forms.compra_forms import CreateCompraForm, UpdateCompraForm
from decorators import login_required
from models.menu_roles import Menu_roles

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
    form=CreateCompraForm()
    if form.validate_on_submit():
        id_ticket = form.id_ticket.data
        id_cliente = form.id_cliente.data
        id_producto = form.id_producto.data
        fecha_compra = form.fecha_compra.data
        cantidad_compra = form.cantidad_compra.data
        total_compra = form.total_compra.data
        com=Compra(id_ticket, id_cliente, id_producto, fecha_compra, cantidad_compra, total_compra)
        com.save()
        return redirect(url_for('compra.compra'))
    return render_template('compra/create_com.html', form=form)

@compra_views.route('/compra/<int:id_compra>/update/', methods=('GET', 'POST'))
def update_com(id_compra):
    form=CompraForm()
    pro=Compra.get(id_compra)
    if form.validate_on_submit():
        com.id_ticket = form.id_ticket.data
        com.id_cliente = form.id_cliente.data
        com.id_producto = form.id_producto.data
        com.fecha_compra = form.fecha_compra.data
        com.cantidad_compra = form.cantidad_compra.data
        com.total_compra = form.total_compra.data
        com.save()
        return redirect(url_for('compra.compra'))
    form.id_ticket.data = com.id_ticket
    form.id_cliente.data = com.id_cliente
    form.id_producto.data = com.id_producto
    form.fecha_compra.data = com.fecha_compra
    form.cantidad_compra.data = com.cantidad_compra
    form.total_compra.data = com.total_compra
    return render_template('compra/create_com.html', form=form)

@compra_views.route('/compra/<int:id_compra>/delete/', methods=('POST',))
def delete_com(id_compra):
    com=Compra.get(id_compra)
    com.delete()
    return redirect(url_for('compra.compra'))