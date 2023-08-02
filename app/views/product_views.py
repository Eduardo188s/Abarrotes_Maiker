from flask import Blueprint, render_template, request, redirect, flash, url_for
from models.products import Product
from forms.product_forms import CreateProductForm, UpdateProductForm

product_views=Blueprint('product',__name__)

from utils.file_handler import save_image

@product_views.route('/producto/')
def producto():
    #Consultas categorias de DB
    productos = Product.get_all()
    return render_template('product/producto.html', producto=productos)

@product_views.route('/producto/create/', methods=('GET', 'POST'))
def create_pro():
    form=CreateProductForm()
    if form.validate_on_submit():
        nombre_producto = form.nombre_producto.data
        marca_producto = form.marca_producto.data
        cb_producto = form.cb_producto.data
        precio_producto = form.precio_producto.data
        f = form.image.data
        image = save_image(f, 'images/products')
        pro=Product(nombre_producto, marca_producto, cb_producto, precio_producto, image)
        pro.save()
        return redirect(url_for('product.producto'))
    return render_template('product/create_pro.html', form=form)

@product_views.route('/producto/<int:id_producto>/update/', methods=('GET', 'POST'))
def update_pro(id_producto):
    form=UpdateProductForm()
    pro=Product.get(id_producto)
    if form.validate_on_submit():
        pro.nombre_producto = form.nombre_producto.data
        pro.marca_producto = form.marca_producto.data
        pro.cb_producto = form.cb_producto.data
        pro.precio_producto = form.precio_producto.data
        f = form.image.data
        pro.image = save_image(f, 'images/products')
        pro.save()
        return redirect(url_for('product.producto'))
    form.nombre_producto.data = pro.nombre_producto
    form.marca_producto.data = pro.marca_producto
    form.cb_producto.data = pro.cb_producto
    form.precio_producto.data = pro.precio_producto
    form.image.data = pro.image
    return render_template('product/create_pro.html', form=form)

@product_views.route('/producto/<int:id_producto>/delete/', methods=('POST',))
def delete_pro(id_producto):
    pro=Product.get(id_producto)
    pro.delete()
    return redirect(url_for('product.producto'))