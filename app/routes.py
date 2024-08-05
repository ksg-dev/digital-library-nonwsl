from flask import Flask, render_template, request, redirect, url_for
from app import app, db
from app.forms import BookForm
from app.models import Book

@app.route('/')
def home():
    return render_template('index.html', library=Book.query.all())


@app.route('/add', methods=["GET", "POST"])
def add():
    if request.method == "POST":
        form = BookForm()
        if form.validate_on_submit():
            title = form.title.data.title()
            author = form.author.data.title()
            rating = form.rating.data

            print(f"{title} - {author} - {rating}")



            # CREATE RECORD
            with app.app_context():
                new_book = Book(title=title, author=author, rating=rating)
                db.session.add(new_book)
                db.session.commit()

                return redirect(url_for('home'))

    return render_template('add.html')


