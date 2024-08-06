from sqlalchemy.orm import Mapped, mapped_column
from app import app, db


class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    author: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[float] = mapped_column(nullable=False)

    def __repr__(self):
        return f"<Book {self.title}>"


# Create table schema in db. Requires app context
with app.app_context():
    db.create_all()


def validate_title(title):
    check = db.session.execute(db.select(Book).filter_by(title=title)).first()
    return check
