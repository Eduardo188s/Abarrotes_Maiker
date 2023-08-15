from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length
from models.products import Product
import datetime

class CreateCompraForm(FlaskForm):
    fecha = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    fecha_compra= StringField('Fecha Compra',
                                default= str(fecha),
                                render_kw={'disabled':''},
                                validators=[DataRequired(),
                                Length(min=3,max=30)])
    
    cantidad_compra=StringField('Cantidad',
                         validators=[DataRequired()])
    
    productosDisponibles = Product.get_all_disponibles()
    productosLista = []
    for p in productosDisponibles:
        productosLista.append((p.id_producto,p.nombre_producto))
    print(productosLista)

    producto = SelectField('Selecciona Producto', validators=[DataRequired()], 
                                                  render_kw={'class':'form-select'},
                                                  choices=productosLista)
    print(productosDisponibles)
    submit=SubmitField('Guardar')

class UpdateCompraForm(FlaskForm):
    fecha_compra=StringField('fecha_compra',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)])
    cantidad_compra=StringField('cantidad_compra',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)])
    
    submit=SubmitField('Actualizar')