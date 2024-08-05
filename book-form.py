from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, URLField
from wtforms.validators import DataRequired, URL

class Book(FlaskForm):
