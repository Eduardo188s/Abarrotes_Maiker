from flask import Blueprint, render_template

home_views=Blueprint('home',__name__)

@home_views.route("/")
def home():
    name = "Eduardo"
    return render_template('home/home.html', name=name)

@home_views.route("/contact/")
def contact():
    user = "Eduardo"
    return render_template('home/contact.html', name=user)