from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class CreateClienteForm(FlaskForm):
    nombre=StringField('Nombre',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)])
    a_materno=StringField('ApellidoMaterno',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)])
    a_paterno=StringField('ApellidoPaterno',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)])
    domicilio=StringField('Domicilio',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)])
    
    submit=SubmitField('Guardar')

class UpdateClienteForm(FlaskForm):
    nombre=StringField('Nombre',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)])
    a_materno=StringField('ApellidoMaterno',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)])
    a_paterno=StringField('ApellidoPaterno',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)])
    domicilio=StringField('Domicilio',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)])
    submit=SubmitField('Actualizar')