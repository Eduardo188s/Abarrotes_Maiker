from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange, Regexp, Email

class CreateProveedorForm(FlaskForm):
    nombre_proveedor = StringField('Nombre',
                               validators=[DataRequired(),
                                           Length(min=3, max=30),
                                           Regexp('^[A-Za-záéíóúÁÉÍÓÚñÑ\s]*$', message='Ingrese solo letras')],
                                render_kw={"placeholder": "Ingresa el nombre"})

    a_paterno=StringField('Apellido Paterno',
                               validators=[DataRequired(),
                                           Length(min=3, max=30),
                                           Regexp('^[A-Za-záéíóúÁÉÍÓÚñÑ\s]*$', message='Ingrese solo letras')],
                                render_kw={"placeholder": "example@gmail.com"})
    
    a_materno=StringField('Apellido Materno',
                               validators=[DataRequired(),
                                           Length(min=3, max=30),
                                           Regexp('^[A-Za-záéíóúÁÉÍÓÚñÑ\s]*$', message='Ingrese solo letras')],
                                render_kw={"placeholder": "Ingresa el Apellido materno"})
    
    marca_proveedor=StringField('Marca',
                               validators=[DataRequired(),
                                           Length(min=3, max=30),
                                           Regexp('^[A-Za-záéíóúÁÉÍÓÚñÑ\s]*$', message='Ingrese solo letras')],
                                render_kw={"placeholder": "Ingresa la Marca"})
    
    direccion_proveedor=StringField('Domicilio',
                               validators=[DataRequired(),
                                           Length(min=3, max=30)],
                                render_kw={"placeholder": "Ingresa el Domicilio"})
    
    correo_proveedor = StringField('Correo',
                               validators=[DataRequired(),
                                           Length(min=3, max=30),
                                           Email(message='Ingrese un correo electrónico válido')],
                                render_kw={"placeholder": "example@gmail.com"})
    
    telefono_proveedor=StringField('Telefono',
                         validators=[DataRequired(),
                                               Length(min=10, max=10)],
                        render_kw={"placeholder": "Ingresa un numero telefonico"})
    
    submit=SubmitField('Guardar')

class UpdateProveedorForm(FlaskForm):    
    nombre_proveedor = StringField('Nombre',
                               validators=[DataRequired(),
                                           Length(min=3, max=30),
                                           Regexp('^[A-Za-záéíóúÁÉÍÓÚñÑ\s]*$', message='Ingrese solo letras')],
                                render_kw={"placeholder": "Ingresa el nombre"})

    a_paterno=StringField('Apellido Paterno',
                               validators=[DataRequired(),
                                           Length(min=3, max=30),
                                           Regexp('^[A-Za-záéíóúÁÉÍÓÚñÑ\s]*$', message='Ingrese solo letras')],
                                render_kw={"placeholder": "Ingresa el Apellido paterno"})
    
    a_materno=StringField('Apellido Materno',
                               validators=[DataRequired(),
                                           Length(min=3, max=30),
                                           Regexp('^[A-Za-záéíóúÁÉÍÓÚñÑ\s]*$', message='Ingrese solo letras')],
                                render_kw={"placeholder": "Ingresa el Apellido materno"})
    
    marca_proveedor =StringField('Marca',
                               validators=[DataRequired(),
                                           Length(min=3, max=30),
                                           Regexp('^[A-Za-záéíóúÁÉÍÓÚñÑ\s]*$', message='Ingrese solo letras')],
                                render_kw={"placeholder": "Ingrese la Marca"})
    
    direccion_proveedor=StringField('Domicilio',
                               validators=[DataRequired(),
                                           Length(min=3, max=30)],
                                render_kw={"placeholder": "Ingresa el Domicilio"})
    
    correo_proveedor = StringField('Correo',
                               validators=[DataRequired(),
                                           Length(min=3, max=30),
                                           Email(message='Ingrese un correo electrónico válido')],
                                render_kw={"placeholder": "example@gmail.com"})
    
    telefono_proveedor=IntegerField('Telefono',
                         validators=[DataRequired(),
                                               NumberRange(min=0)],
                        render_kw={"placeholder": "Ingresa un numero telefonico"})
    
    submit=SubmitField('Actualizar')