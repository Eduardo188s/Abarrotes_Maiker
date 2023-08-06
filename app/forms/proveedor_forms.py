from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

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
    
    telefono_proveedor=StringField('Telefono',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)])
    
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
    
    telefono_proveedor=StringField('Telefono',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)])
    
    submit=SubmitField('Actualizar')