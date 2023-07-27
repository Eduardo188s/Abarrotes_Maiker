from flask import Blueprint, render_template, request, redirect, flash, url_for

from models.proveedor import Proveedor

from forms.proveedor_forms import CreateProveedorForm, UpdateProveedorForm

proveedor_views = Blueprint('proveedor',__name__)

@proveedor_views.route('/proveedor/')
def proveedor():
    #Consultas categorias de DB
    proveedor = Proveedor.get_all()
    return render_template('proveedor/proveedor.html', proveedor=proveedor)

@proveedor_views.route('/proveedor/create/', methods=('GET', 'POST'))
def create_pro():
    form=CreateProveedorForm()
    if form.validate_on_submit():
        nombre_proveedor = form.nombre_proveedor.data
        a_paterno = form.a_paterno.data
        a_materno = form.a_materno.data
        direccion_proveedor = form.direccion_proveedor.data
        correo_proveedor = form.correo_proveedor.data
        telefono_proveedor = form.telefono_proveedor.data
        prov=Proveedor(nombre_proveedor, a_paterno, a_materno, direccion_proveedor, correo_proveedor, telefono_proveedor)
        prov.save()
        return redirect(url_for('proveedor.proveedor'))
    return render_template('proveedor/create_prov.html', form=form)


@proveedor_views.route('/proveedor/<int:id>/update/', methods=('GET', 'POST'))
def update_pro(id_producto):
    form=UpdateProveedorForm()
    prov=Proveedor.get(id)
    if form.validate_on_submit():
        nombre_proveedor = form.nombre_proveedor.data
        a_paterno = form.a_paterno.data
        a_materno = form.a_materno.data
        direccion_proveedor = form.direccion_proveedor.data
        correo_proveedor = form.correo_proveedor.data
        telefono_proveedor = form.telefono_proveedor.data
        
        pro.save()
        return redirect(url_for('proveedor.proveedor'))
    form.nombre_proveedor.data=pro.nombre_proveedor
    form.a_paterno_proveedor.data=pro.aPaterno_proveedor_proveedor
    form.a_materno_proveedor.data=pro.aMaterno_proveedor_proveedor
    form.direccion_proveedor_proveedor.data=pro.direccion_proveedor_proveedor
    form.correo_proveedor_proveedor.data=pro.correo_proveedor_proveedor
    form.telefono_proveedor_proveedor.data=pro.telefono_proveedor_proveedor
    return render_template('proveedor/create_prov.html', form=form)


@proveedor_views.route('/proveedor/<int:id_proveedor>/delete/', methods=('POST',))
def delete_pro(id_producto):
    pro=Proveedor.get(id)
    pro.delete()
    return redirect(url_for('proveedor.proveedor'))