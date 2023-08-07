from flask import Blueprint, render_template, request, redirect, flash, url_for, session
from models.proveedor import Proveedor
from forms.proveedor_forms import CreateProveedorForm, UpdateProveedorForm
from decorators import login_required
from models.menu_roles import Menu_roles
proveedor_views = Blueprint('proveedor',__name__)

@proveedor_views.route('/proveedor/')
@ login_required
def proveedor():
    nav = Menu_roles.get(session.get("role"))
    #Consultas categorias de DB
    proveedores = Proveedor.get_all()
    return render_template('proveedor/proveedor.html', nav = nav, proveedor=proveedores)

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


@proveedor_views.route('/proveedor/<int:id_proveedor>/update/', methods=('GET', 'POST'))
def update_prov(id_proveedor):
    form=UpdateProveedorForm()
    prov=Proveedor.get(id_proveedor)
    if form.validate_on_submit():
        prov.nombre_proveedor = form.nombre_proveedor.data
        prov.a_paterno = form.a_paterno.data
        prov.a_materno = form.a_materno.data
        prov.direccion_proveedor = form.direccion_proveedor.data
        prov.correo_proveedor = form.correo_proveedor.data
        prov.telefono_proveedor = form.telefono_proveedor.data
        prov.save()
        return redirect(url_for('proveedor.proveedor'))
    form.nombre_proveedor.data=prov.nombre_proveedor
    form.a_paterno.data=prov.a_paterno
    form.a_materno.data=prov.a_materno
    form.direccion_proveedor.data=prov.direccion_proveedor
    form.correo_proveedor.data=prov.correo_proveedor
    form.telefono_proveedor.data=prov.telefono_proveedor
    return render_template('proveedor/create_prov.html', form=form)


@proveedor_views.route('/proveedor/<int:id_proveedor>/delete/', methods=('POST',))
def delete_prov(id_proveedor):
    prov=Proveedor.get(id_proveedor)
    prov.delete()
    return redirect(url_for('proveedor.proveedor'))