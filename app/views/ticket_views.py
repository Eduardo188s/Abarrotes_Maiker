from flask import Blueprint, render_template, session,request
from decorators import login_required
from models.menu_roles import Menu_roles
from models.detalle import Detalle

ticket_views=Blueprint('ticket',__name__)


@ticket_views.route('/ticket/')
@ login_required
def create_com():
    nav = Menu_roles.get(session.get("role"))
    
    listaTicket = []

    if request.args.__len__() > 0:
        id_compra = request.args["id_compra"]
        if id_compra:
            listaTicket = Detalle.get(id_compra)

        return render_template('ticket/ticket.html',  nav = nav, listaTicket = listaTicket)
    return render_template('ticket/ticket.html',  nav = nav, listaTicket = listaTicket)


