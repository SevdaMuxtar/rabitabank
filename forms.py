from cProfile import label
from random import choices
from wsgiref.validate import validator
from wtforms import StringField, TextAreaField, EmailField, SelectField, DateField, TimeField, RadioField
from wtforms.validators import DataRequired, Email, Length
from flask_wtf import FlaskForm
from models import *



class OnlineQueueForm(FlaskForm):
    filial_name = SelectField(label=('Filial seçin'), validators=[DataRequired()], choices=[(filial.id, filial.name) for filial in Filial.query.all()])
    service_type = SelectField(label=('Xidmət növü seçin'), validators=[DataRequired()], choices=[(servicex.id, servicex.name) for servicex in ServiceType.query.all()])
    date = DateField(label=('Tarixi seçin'), validators=[DataRequired()])
    time = SelectField(label=('Vaxtı seçin'), validators=[DataRequired()], choices=[(time.id, time.hour) for time in Time.query.all()])
    phone_number = StringField(label=('form-field'), validators=[DataRequired(), Length(max=20)])


class OnlineDepositsForm(FlaskForm):
    name = StringField(label=('Adınız'), validators=[DataRequired(), Length(max=255)])
    surname = StringField(label=('Soyadınız'), validators=[DataRequired(), Length(max=255)])
    phone_number = StringField(label=('Mobil nömrəniz'), validators=[DataRequired(), Length(max=40)])
    deposit_type = RadioField(label=('Əmanətin növü'), validators=[DataRequired()], choices=[(deposit_type.id, deposit_type.deposit_name) for deposit_type in DepositType.query.all()])
