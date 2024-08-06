from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import InputRequired
from app import db


class BookForm(FlaskForm):
    title = StringField('Book Title', validators=[InputRequired()])
    author = StringField('Author', validators=[InputRequired()])
    rating = FloatField('Rating', validators=[InputRequired()])
    submit = SubmitField("Add Book")

    # def validate_title(self, title):
    #     book = db.session.scalars()
