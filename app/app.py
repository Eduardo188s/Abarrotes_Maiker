from flask import Flask, request, session, redirect,url_for

from flask_session import Session

# Import from Views
from views.home_views import home_views
from views.product_views import product_views
from views.proveedor_views import proveedor_views
from views.cliente_views import cliente_views
from views.compra_views import compra_views
from views.user_views import user_views
from views.error_views import error_views
from views.ticket_views import ticket_views

app = Flask(__name__)

app.config['SECRET_KEY'] = 'my secret key'

# app.config["SESSION_PERMANET"] = False
# app.config["SESSION TYPO"] = "filesystem"

# Session(app)

app.register_blueprint(home_views)
app.register_blueprint(product_views)
app.register_blueprint(proveedor_views)
app.register_blueprint(cliente_views)
app.register_blueprint(compra_views)
app.register_blueprint(user_views)
app.register_blueprint(error_views)

#app.register_blueprint(ticket_views)

if __name__ == '__main__':
    app.run(debug=True)

