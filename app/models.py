from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, validates
from sqlalchemy import Integer, String, Float
from app import app, db


class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    author: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[float] = mapped_column(nullable=False)

    def __repr__(self):
        return f"<Book {self.title}>"

    # @validates("title")
    # def validate_title(self, key, title):
    #     if not title:
    #         raise AssertionError("Please enter book title")
    #
    #     if Book.query.filter(Book.title == title).first():
    #         raise AssertionError("Title already in database")
    #
    #     return title
    #
    # @validates("author")
    # def validate_author(self, author):
    #     if not author:
    #         raise AssertionError("Please enter author")
    #
    #     return author
    #
    # @validates("rating")
    # def validate_rating(self, rating):
    #     if not rating:
    #         raise AssertionError("Please enter rating on scale of 0.0 to 10.0")
    #
    #     if rating < 0 or rating > 10:
    #         raise AssertionError("Please enter rating on scale of 0.0 to 10.0")
    #
    #     return rating



# Create table schema in db. Requires app context
with app.app_context():
    db.create_all()