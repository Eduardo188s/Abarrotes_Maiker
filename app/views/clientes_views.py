from flask import Blueprint, render_template, request, redirect, flash, url_for

from models.cliente import Cliente

from forms.clientes_forms import CreateClienteForm, UpdateClienteForm

clientes_views=Blueprint('clientes',__name__)

@clientes_views.route('/cliente/')
def cliente():
    #Consultas categorias de DB
    cliente = Cliente.get_all()
    return render_template('clientes/clientes.html', product=producto)

@clientes_views.route('/cliente/create/', methods=('GET', 'POST'))
def create_cli():
    form=CreateClientetForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        a_paterno = form.a_paterno.data
        a_materno = form.a_materno.data
        domicilio = form.domicilio.data
        cli=Cliente(nombre, a_paterno, a_materno, domicilio)
        cli.save()
        return redirect(url_for('clientes.clientes'))
    return render_template('clientes/create_cli.html', form=form)


@clientes_views.route('/cliente/<int:id>/update/', methods=('GET', 'POST'))
def update_cli(id_cliente):
    form=UpdateClienteForm()
    cli=Cliente.get(id)
    if form.validate_on_submit():
        nombre = form.nombre.data
        a_paterno = form.a_paterno.data
        a_materno = form.a_materno.data
        domicilio = form.domicilio.data
        cli.save()
        return redirect(url_for('clientes.clientes'))
    form.nombre.data=cli.nombre
    form.a_paterno.data=cli.a_paterno
    form.a_materno.data=cli.a_materno
    form.domicilio.data=cli.domicilio
    return render_template('clientes/create_cli.html', form=form)


@clientes_views.route('/clientes/<int:id_cliente>/delete/', methods=('POST',))
def delete_cli(id_cliente):
    cli=Cliente.get(id)
    cli.delete()
    return redirect(url_for('clientes.clientes'))