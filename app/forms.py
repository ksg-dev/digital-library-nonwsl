from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import InputRequired, NumberRange



class BookForm(FlaskForm):
    title = StringField('Book Title',
                        validators=[
                            InputRequired()
                        ]
                        )
    author = StringField('Author',
                         validators=[
                             InputRequired()
                         ]
                         )
    rating = FloatField('Rating',
                        validators=[
                            InputRequired(),
                            NumberRange(min=0, max=10, message="Please enter a rating between 0.0 and 10.0")
                        ]
                        )
    submit = SubmitField("Add Book")

    # def validate_title(self, title):
    #      if Book.query
