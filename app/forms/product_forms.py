from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, FloatField,  IntegerField, validators, DecimalField
from wtforms.validators import DataRequired, Length, NumberRange
from flask_wtf.file import FileField, FileAllowed


class CreateProductForm(FlaskForm):
    nombre_producto = StringField('Nombre',
                              validators=[DataRequired(),
                                          Length(min=3, max=30)],
                              render_kw={"placeholder": "Ingresa el nombre del producto"})

    
    marca_producto=StringField('Marca',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)],
                         render_kw={"placeholder": "Ingresa la marca del producto"})
    
    cb_producto=StringField('CB', validators=[
        validators.DataRequired(message="Este campo es requerido."),
        validators.Length(min=13, max=13, message="El código de barras debe tener exactamente 15 dígitos."),
        validators.Regexp(r'^\d+$', message="El código de barras debe contener solo dígitos.")],
        render_kw={"placeholder": "Ingresa el codigo de barras"})

    precio_producto = DecimalField('Precio',  # Cambio aquí
                                   validators=[DataRequired(),
                                               NumberRange(min=0)],  # No se necesita max=None para enteros
                                    render_kw={"placeholder": "Ingresa el precio del producto"})
    
    existencia= IntegerField('Existencia',  # Cambio aquí
                                   validators=[DataRequired(),
                                               NumberRange(min=0)], # No se necesita max=None para enteros
                                    render_kw={"placeholder": "Ingresa la existencia del producto"})

                                     
    
    submit=SubmitField('Guardar')

class UpdateProductForm(FlaskForm):
    nombre_producto = StringField('Nombre',
                              validators=[DataRequired(),
                                          Length(min=3, max=30)],
                              render_kw={"placeholder": "Ingresa el nombre del producto"})

    
    marca_producto=StringField('Marca',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)],
                         render_kw={"placeholder": "Ingresa la marca del producto"})
    
    cb_producto=StringField('CB', validators=[
        validators.DataRequired(message="Este campo es requerido."),
        validators.Length(min=13, max=13, message="El código de barras debe tener exactamente 15 dígitos."),
        validators.Regexp(r'^\d+$', message="El código de barras debe contener solo dígitos.")],
        render_kw={"placeholder": "Ingresa el codigo de barras"})

    precio_producto = DecimalField('Precio',  # Cambio aquí
                                   validators=[DataRequired(),
                                               NumberRange(min=0)],  # No se necesita max=None para enteros
                                    render_kw={"placeholder": "Ingresa el precio del producto"})
    
    existencia= IntegerField('Existencia',  # Cambio aquí
                                   validators=[DataRequired(),
                                               NumberRange(min=0)], # No se necesita max=None para enteros
                                    render_kw={"placeholder": "Ingresa la existencia del producto"})
                                     
    submit=SubmitField('Actualizar')