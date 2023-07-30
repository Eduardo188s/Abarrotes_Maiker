from flask import Blueprint, render_template, request, redirect, flash, url_for
from models.cliente import Cliente
from forms.cliente_forms import CreateClienteForm, UpdateClienteForm

cliente_views=Blueprint('cliente',__name__)

@cliente_views.route('/cliente/')
def cliente():
    #Consultas categorias de DB
    clientes = Cliente.get_all()
    return render_template('cliente/cliente.html', cliente=clientes)

@cliente_views.route('/cliente/create/', methods=('GET', 'POST'))
def create_cli():
    form=CreateClienteForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        a_paterno = form.a_paterno.data
        a_materno = form.a_materno.data
        domicilio = form.domicilio.data
        cli=Cliente(nombre, a_paterno, a_materno, domicilio)
        cli.save()
        return redirect(url_for('cliente.cliente'))
    return render_template('cliente/create_cli.html', form=form)


@cliente_views.route('/cliente/<int:id_cliente>/update/', methods=('GET', 'POST'))
def update_cli(id_cliente):
    form=UpdateClienteForm()
    cli=Cliente.get(id_cliente)
    if form.validate_on_submit():
        cli.nombre = form.nombre.data
        cli.a_paterno = form.a_paterno.data
        cli.a_materno = form.a_materno.data
        cli.domicilio = form.domicilio.data
        cli.save()
        return redirect(url_for('cliente.cliente'))
    form.nombre.data=cli.nombre
    form.a_paterno.data=cli.a_paterno
    form.a_materno.data=cli.a_materno
    form.domicilio.data=cli.domicilio
    return render_template('cliente/create_cli.html', form=form)


@cliente_views.route('/cliente/<int:id_cliente>/delete/', methods=('POST',))
def delete_cli(id_cliente):
    cli=Cliente.get(id_cliente)
    cli.delete()
    return redirect(url_for('cliente.cliente'))