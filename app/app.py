from flask import Flask, request, session, redirect
from models.menu_roles  import Menu_roles
from models.menus import Menus
# Import from Views
from views.home_views import home_views
from views.product_views import product_views
from views.proveedor_views import proveedor_views
from views.cliente_views import cliente_views
from views.compra_views import compra_views
from views.user_views import user_views
from views.error_views import error_views


app = Flask(__name__)
app.config['SECRET_KEY'] = 'my secret key'

@user_views.before_request
def middleware():
    print("Sesion")
    print(session)
    ruta = request.path
    menu_rol =[]
    menus = []

    menus = Menus.get_all()

    if not "user" in session:
        menu_rol =  Menu_roles.get(3)
    else:
        menu_rol =  Menu_roles.get(session.get("role"))

    if len(filter(lambda x: x.ruta == ruta, menus)) == 0:
        redirect("/")

    for m in menu_rol:
       

        else :   
            if m.ruta != ruta:
                redirect("/")







app.register_blueprint(home_views)
app.register_blueprint(product_views)
app.register_blueprint(proveedor_views)
app.register_blueprint(cliente_views)
app.register_blueprint(compra_views)
app.register_blueprint(user_views)
app.register_blueprint(error_views)

if __name__ == '__main__':
    app.run(debug=True)