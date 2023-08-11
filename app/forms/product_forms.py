from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, FloatField,  IntegerField, validators 
from wtforms.validators import DataRequired, Length, NumberRange, Regexp
from flask_wtf.file import FileField, FileAllowed


class CreateProductForm(FlaskForm):

    nombre_producto=StringField('Nombre',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)])
    marca_producto=StringField('Marca',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)])
    cb_producto=StringField('CB', validators=[
        validators.DataRequired(message="Este campo es requerido."),
        validators.Length(min=10, max=15, message="El código de barras debe tener exactamente 15 dígitos."),
        validators.Regexp(r'^\d+$', message="El código de barras debe contener solo dígitos.")])

    precio_producto = IntegerField('Precio',  # Cambio aquí
                                   validators=[DataRequired(),
                                               NumberRange(min=0)])  # No se necesita max=None para enteros
    existencia= IntegerField('Existencia',  # Cambio aquí
                                   validators=[DataRequired(),
                                               NumberRange(min=0)])  # No se necesita max=None para enteros

                                     
    
    submit=SubmitField('Guardar')

class UpdateProductForm(FlaskForm):
    nombre_producto=StringField('Nombre',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)])
    marca_producto=StringField('Marca',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)])
    cb_producto=StringField('CB', validators=[
        validators.DataRequired(message="Este campo es requerido."),
        validators.Length(min=10, max=15, message="El código de barras debe tener exactamente 15 dígitos."),
        validators.Regexp(r'^\d+$', message="El código de barras debe contener solo dígitos y letras en mayusculas.")])
    precio_producto = IntegerField('Precio',  # Cambio aquí
                                   validators=[DataRequired(),
                                               NumberRange(min=0)])
    existencia= IntegerField('Existencia',  # Cambio aquí
                                   validators=[DataRequired(),
                                               NumberRange(min=0)]) 
                                     
    submit=SubmitField('Actualizar')