from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,SelectField
from wtforms.validators import DataRequired


class InputForm(FlaskForm):
    articles = SelectField('article',choices=[('LNCS_9678','(LNCS_9678) ESWC2016 Main Conference'),('CCIS_641','(CCIS_641) ESWC2016 Challenges')])
    submit = SubmitField('Extract')

