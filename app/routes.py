from flask import Flask, render_template, request, redirect, url_for, jsonify
from app import app, db
from app.forms import BookForm
from app.models import Book
from flask_sqlalchemy import SQLAlchemy


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

            # if form.validate_on_submit():

            # print("SUCCESS")
            print(f"{title} - {author} - {rating}")

            # Check for title
            # title_check = db.session.scalar(SQLAlchemy.select(Book).where(Book.title == title))
            # if title_check is None:
            #     # flash("Title already in database")
            #     print("Title verified")

            new_book = Book(title=title, author=author, rating=rating)

            try:
                db.session.add(new_book)
                db.session.commit()
                print("Success")
                return redirect(url_for('home'))

            except AssertionError as exception_message:
                return jsonify(msg="Error: {}. ".format(exception_message))

    return render_template('add.html', form=form)


