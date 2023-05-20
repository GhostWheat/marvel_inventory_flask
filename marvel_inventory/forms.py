from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DecimalField
from wtforms.validators import DataRequired, Email

class UserLoginForm(FlaskForm):
    # email, password, submit_button
    username = StringField('Username', validators =[DataRequired()])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit_button = SubmitField()

class HeroForm(FlaskForm):
    hero_name = StringField('Name')
    description = StringField('Description')
    comics_appeared_in = DecimalField('Number of Comics', places=0)
    super_power = StringField('Super Power')
    submit_button = SubmitField('Add This Hero!')
    