from flask import Blueprint, render_template, request, redirect, flash, url_for, Flask, session
from models.products import Product
from decorators import login_required
from forms.product_forms import CreateProductForm, UpdateProductForm
from utils.file_handler import save_image
from models.menu_roles import Menu_roles


product_views=Blueprint('product',__name__)

@product_views.route('/producto/')
@ login_required
def producto():

    nav = Menu_roles.get(session.get("role"))

    #Consultas categorias de DB
    productos = Product.get_all()
    return render_template('product/producto.html', nav = nav, producto=productos)

@product_views.route('/producto/create/', methods=('GET', 'POST'))
def create_pro():
    
    nav = Menu_roles.get(session.get("role"))
    form=CreateProductForm()
    if form.validate_on_submit():
        nombre_producto = form.nombre_producto.data
        marca_producto = form.marca_producto.data
        cb_producto = form.cb_producto.data
        precio_producto = form.precio_producto.data
        existencia = form.existencia.data
        pro=Product(nombre_producto, marca_producto, cb_producto, precio_producto, existencia)
        pro.save()
        return redirect(url_for('product.producto'))
    return render_template('product/create_pro.html', form=form, nav =nav)

@product_views.route('/producto/<int:id_producto>/update/', methods=('GET', 'POST'))
@ login_required
def update_pro(id_producto):
    nav = Menu_roles.get(session.get("role"))
    form=UpdateProductForm()
    pro=Product.get(id_producto)
    if form.validate_on_submit():
        pro.nombre_producto = form.nombre_producto.data
        pro.marca_producto = form.marca_producto.data
        pro.cb_producto = form.cb_producto.data
        pro.precio_producto = form.precio_producto.data
        pro.existencia = form.existencia.data
        pro.save()
        return redirect(url_for('product.producto'))
    form.nombre_producto.data = pro.nombre_producto
    form.marca_producto.data = pro.marca_producto
    form.cb_producto.data = pro.cb_producto
    form.precio_producto.data = pro.precio_producto
    form.existencia.data = pro.existencia
    return render_template('product/create_pro.html', form=form, nav=nav)

@product_views.route('/producto/<int:id_producto>/delete/', methods=('POST',))
def delete_pro(id_producto):
    pro=Product.get(id_producto)
    pro.delete()
    return redirect(url_for('product.producto'))