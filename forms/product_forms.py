from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

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
    precio_producto=StringField('Precio',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)])
    
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
    precio_producto=StringField('Precio',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)])
    submit=SubmitField('Actualizar')