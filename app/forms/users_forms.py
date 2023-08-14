from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, EmailField, SelectField,
                     SubmitField, ValidationError)
from wtforms.validators import DataRequired, Email, EqualTo, Length
from flask_wtf.file import FileField, FileRequired, FileAllowed

from models.users import User

################# Formulario de Registro ##################
class RegisterForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()],render_kw={"placeholder": "Ingresa un Usuario"})
    email = EmailField('Email', validators=[DataRequired(), Email()],render_kw={"placeholder": "Ingresa en correo electronico"})
    password = PasswordField('Contraseña', validators=[DataRequired(),
                                                    EqualTo('password_confirm', 
                                                            message='Las contraseñas deben coincidir')],
                                        render_kw={"placeholder": "Ingresa la contraseña"})
    role = SelectField('Selecciona Rol', choices=[],  coerce=int, validate_choice=False)
    password_confirm = PasswordField('Confirmar contraseña', validators=[DataRequired()],render_kw={"placeholder": "Confirma la contraseña"})
    submit = SubmitField('Registrar')

    ######## Validar Correo Unico #########
    def validate_email(self, field):
        ######## Consultar si el correo existe en la base de datos #######
        if User.check_email(field.data):
            raise ValidationError('El correo ya existe')

    ######## Validar Username Unico #########
    def validate_username(self, field):
        ######## Consultar si el username existe en la base de datos #######
        if User.check_username(field.data):
            raise ValidationError('El username ya existe')

class RegisterUserAdmin(RegisterForm):
    role = SelectField('role', choices=[('admin', 'Administrador'), ('cajero', 'Cajero')])

################# Formulario de Login ##################
class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()],render_kw={"placeholder": "Ingresa tu Usuario"})
    password = PasswordField('Contraseña', validators=[DataRequired()],render_kw={"placeholder": "Ingresa tu Contraseña"})
    submit = SubmitField('Ingresar')

################ Formulario de Perfil ################
class ProfileForm(FlaskForm):
    # username No se edita
    # password No se edita
    # email, Verificar antes de actualizar
    first_name = StringField('Nombre',
                             validators=[DataRequired(), Length(min=3, max=30)])
    last_name = StringField('Apellidos', 
                            validators=[DataRequired(), Length(min=10, max=40)])
    image = FileField('Imagen de Perfil', 
                      validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Solo imagenes!')])
    submit = SubmitField('Actualizar')