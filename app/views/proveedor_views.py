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
def create_prov():
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
def update_prov(id_producto):
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
    form.nombre_proveedor.data=prov.nombre_proveedor
    form.a_paterno.data=prov.aPaterno_proveedor_proveedor
    form.a_materno.data=prov.aMaterno_proveedor_proveedor
    form.direccion_proveedor_proveedor.data=prov.direccion_proveedor_proveedor
    form.correo_proveedor_proveedor.data=prov.correo_proveedor_proveedor
    form.telefono_proveedor_proveedor.data=prov.telefono_proveedor_proveedor
    return render_template('proveedor/create_prov.html', form=form)


@proveedor_views.route('/proveedor/<int:id_proveedor>/delete/', methods=('POST',))
def delete_prov(id_provedor):
    prov=Proveedor.get(id)
    prov.delete()
    return redirect(url_for('proveedor.proveedor'))