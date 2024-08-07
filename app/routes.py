from flask import Flask, render_template, request, redirect, url_for, jsonify
from app import app, db
from app.forms import BookForm
from app.models import Book, validate_title
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5

bootstrap = Bootstrap5(app)

@app.route('/')
def home():
    return render_template('index.html', library=Book.query.all())


@app.route('/add', methods=["GET", "POST"])
def add():
    form = BookForm()
    if request.method == "POST":
        if form.validate_on_submit():
            title = form.title.data.title()
            author = form.author.data.title()
            rating = form.rating.data

            # print(f"{title} - {author} - {rating}")

            # Check for title
            title_check = validate_title(title)

            if title_check is None:
                print("Title verified")

                new_book = Book(title=title, author=author, rating=rating)

                with app.app_context():
                    db.session.add(new_book)
                    db.session.commit()

                return redirect(url_for("home"))

            else:
                return render_template('add.html', error=f"Title already in database.\n\n", form=form)

    return render_template('add.html', error=None, form=form)

@app.route("/book/<int:num>")
def get_book(num):
    target_book = db.session.execute(db.select(Book).filter_by(id=num)).first()
    print(target_book)
    return render_template("record.html", book=target_book)

@app.route("/search")
def search():
    search_for = request.form["search"]
    search_terms = db.session.execute(db.select(Book).where(Book.title == f'%{search_for}%')).scalars()
    return render_template("search.html", query_results=search_terms)
