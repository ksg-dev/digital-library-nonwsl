from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField
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
    rating = DecimalField('Rating',
                        validators=[
                            InputRequired(),
                            NumberRange(min=0, max=10, message="Please enter a rating between 0.0 and 10.0")
                        ],
                          places=1
                        )
    submit = SubmitField("Add Book")