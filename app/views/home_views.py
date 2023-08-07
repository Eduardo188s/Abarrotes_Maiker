from flask import Blueprint, render_template,session
from models.menu_roles import Menu_roles

home_views=Blueprint('home',__name__)

@home_views.route("/")
def home():
    name = "Eduardo"
 
    if "role" in session and session.get("role") :
        print(session.get("role"))
        nav = Menu_roles.get(session.get("role"))
        print(len(nav))
        return render_template('home/home.html',nav =nav, name=name)


   
    return render_template('home/home.html', name=name)

@home_views.route("/contact/")
def contact():
    user = "Eduardo"
    return render_template('home/contact.html', name=user)