from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange

class CreateProveedorForm(FlaskForm):
    nombre_proveedor=StringField('Nombre',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)])
    a_paterno=StringField('ApellidoPaterno',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)])
    a_materno=StringField('ApellidoMaterno',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)])
    direccion_proveedor=StringField('Direccion',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)])
    correo_proveedor=StringField('Correo',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)])
    
    telefono_proveedor=IntegerField('Telefono',
                         validators=[DataRequired(),
                                               NumberRange(min=0)])
    
    submit=SubmitField('Guardar')

class UpdateProveedorForm(FlaskForm):    

    nombre_proveedor=StringField('Nombre',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)])
    a_paterno=StringField('ApellidoPaterno',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)])
    a_materno=StringField('ApellidoMaterno',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)])
    direccion_proveedor=StringField('Direccion',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)])
    correo_proveedor=StringField('Correo',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)])
    
    telefono_proveedor=IntegerField('Telefono',
                         validators=[DataRequired(),
                                               NumberRange(min=0)])
    
    submit=SubmitField('Actualizar')