from flask import Flask, render_template, request, redirect, url_for, jsonify
from app import app, db
from app.forms import BookForm
from app.models import Book, validate_title
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5

bootstrap = Bootstrap5(app)




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
    target_book = db.session.execute(db.select(Book).filter_by(id=num)).scalars().first()
    print(target_book)
    return render_template("record.html", book=target_book)

@app.route("/search/<terms>")
def search(terms):
    # query_terms = request.args.get("q")
    # print(f"search function: {query_terms}")

    search_for = db.session.execute(db.select(Book).filter(Book.title.like(f"%{terms}%"))).scalars().all()

    search_results = []
    for i in search_for:
        print(i.id, i.title, i.author, i.rating)
    return render_template("search.html", query_results=search_for)

@app.route('/', methods=["GET", "POST"])
def home():
    query = request.args.get("q")
    print(query)
    if query is not None:
        return redirect(url_for('search', terms=query))

    else:
        return render_template('index.html', library=Book.query.all(), query=None)