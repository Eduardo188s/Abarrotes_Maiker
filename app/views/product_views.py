from flask import Blueprint, render_template, request, redirect, flash, url_for
from models.products import Product
from forms.product_forms import CreateProductForm, UpdateProductForm

product_views=Blueprint('product',__name__)

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
        pro=Product(nombre_producto, marca_producto, cb_producto, precio_producto)
        pro.save()
        return redirect(url_for('product.producto'))
    return render_template('product/create_pro.html', form=form)

@product_views.route('/producto/<int:id_producto>/update/', methods=('GET', 'POST'))
def update_pro(id_producto):
    pro=Product.get(id_producto)
    form=UpdateProductForm(obj=pro)
    if form.validate_on_submit():
        form.populate_obj(pro)
        pro.save()
        return redirect(url_for('product.producto'))
    return render_template('product/create_pro.html', form=form)

@product_views.route('/producto/<int:id_producto>/delete/', methods=('POST',))
def delete_pro(id_producto):
    pro=Product.get(id_producto)
    pro.delete()
    return redirect(url_for('product.producto'))