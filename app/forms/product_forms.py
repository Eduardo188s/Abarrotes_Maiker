from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, FloatField
from wtforms.validators import DataRequired, Length, NumberRange
from flask_wtf.file import FileField, FileAllowed


class CreateProductForm(FlaskForm):

    nombre_producto=StringField('Nombre',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)])
    marca_producto=StringField('Marca',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)])
    cb_producto=StringField('CB',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)])
    precio_producto=FloatField('Precio',
                         validators=[DataRequired(),
                                     NumberRange(min=0.0, max=None)])

    image = FileField('Imagen de Producto', 
                      validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Solo imagenes!')])
                                     
    
    submit=SubmitField('Guardar')

class UpdateProductForm(FlaskForm):
    nombre_producto=StringField('Nombre',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)])
    marca_producto=StringField('Marca',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)])
    cb_producto=StringField('CB',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)])
    precio_producto=FloatField('Precio',
                         validators=[DataRequired(),
                                    NumberRange(min=0.0, max=None)])
                                     

    image = FileField('Imagen de Producto', 
                      validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Solo imagenes!')])
    submit=SubmitField('Actualizar')