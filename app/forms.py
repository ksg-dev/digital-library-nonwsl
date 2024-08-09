from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField, HiddenField
from wtforms.validators import InputRequired, NumberRange, ValidationError
from app import db
from app.models import Book



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

class EditBookForm(FlaskForm):
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
    submit = SubmitField("Update Record")

    def __init__(self, og_title, key, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.og_title = og_title
        self.key = key

    def validate_edit_title(self, title):
        if title.data != self.og_title:
            book = db.session.execute(db.select(Book).where(Book.title == title.data)).scalars()

            if book is not None:
                raise ValidationError("Title already exists in database, please pick a different title")

