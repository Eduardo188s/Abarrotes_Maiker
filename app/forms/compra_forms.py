from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class CreateCompraForm(FlaskForm):
    id_ticket=StringField('id_ticket',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)])
    id_cliente=StringField('id_cliente',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)])
    id_producto=StringField('id_producto',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)])
    fecha_compra=StringField('fecha_compra',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)])
    cantidad_compra=StringField('cantidad_compra',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)])
    
    total_compra=StringField('total_compra',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)])
    
    submit=SubmitField('Guardar')

class UpdateCompraForm(FlaskForm):
    id_ticket=StringField('id_ticket',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)])
    id_cliente=StringField('id_cliente',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)])
    id_producto=StringField('id_producto',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)])
    fecha_compra=StringField('fecha_compra',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)])
    cantidad_compra=StringField('cantidad_compra',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)])
    
    total_compra=StringField('total_compra',
                         validators=[DataRequired(),
                                     Length(min=3,max=30)])
    submit=SubmitField('Actualizar')