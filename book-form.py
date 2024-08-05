from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.validators import DataRequired


class BookForm(FlaskForm):
    title = StringField('Book Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    rating = FloatField('Rating', validators=[DataRequired()])

    # def validate_title(self, title):
    #     book = db.session.scalar()
