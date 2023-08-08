from flask import Blueprint, Flask, redirect, render_template, url_for, flash, abort, request, session
from flask_session import Session
from models.menu_roles import Menu_roles
from models.users import User
from decorators import login_required
from forms.users_forms import LoginForm, RegisterForm, ProfileForm, RegisterUserAdmin
from utils.file_handler import save_image


user_views=Blueprint('user',__name__)

app = Flask(__name__)

app.config["SESSION_PERMANET"] = False
app.config["SESSION TYPO"] = "filesystem"
Session(app)


@user_views.route('/users/register/', methods=('GET', 'POST'))
@ login_required
def register(): 
    nav = Menu_roles.get(session.get("role"))
    form = RegisterUserAdmin()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        role=request.form["role"]

        user = User(username, password, email, role=role)
        user.save()

        return redirect(url_for('user.login'))
    return render_template('user/register.html', form=form, nav = nav)

@user_views.route('/users/login/', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.get_by_password(username, password)
       
        
        if not user:
            flash('Verifica tus Datos')
        else:
            session["name"] = username
            session["id"] = user.id
            session["role"] = user.role
            if "role" in session and session.get("role") :
                print(session.get("role"))
                nav = Menu_roles.get(session.get("role"))
                print(len(nav))
                return render_template('home/home.html',nav =nav, user=user)
            else:
                return render_template('home/home.html', user=user)
    return render_template('user/login.html', form=form)

@user_views.route('/users/logout/', methods=('GET', 'POST'))
def logout():
    form = LoginForm()

    session["name"] = None
    session["role"] = None
    return render_template('home/home.html', form=form)

@user_views.route('/users/<int:id>/profile/', methods=('GET', 'POST'))
@ login_required
def profile(id):

    nav = Menu_roles.get(session.get("role"))

    form = ProfileForm()
    user = User.__get__(id)
    if not user:
        abort(404)
    if form.validate_on_submit():
        user.first_name = form.first_name.data
        user.last_name = form.last_name.data
        f = form.image.data
        if f:
            user.image = save_image(f, 'images/profiles', user.username)
        user.save()
    form.first_name.data = user.first_name
    form.last_name.data = user.last_name
    image = user.image
    return render_template('user/profile.html', form=form, nav=nav, image=image)

