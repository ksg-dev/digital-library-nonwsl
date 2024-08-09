from flask import Flask, render_template, request, redirect, url_for, flash
from app import app, db
from app.forms import BookForm, EditBookForm
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

@app.route("/book/<int:num>/update", methods=["GET", "POST"])
def update(num):
    book_to_update = db.session.execute(db.select(Book).where(Book.id == num)).scalar()
    form = BookForm(obj=book_to_update)

    og_title = form.title.data
    og_author = form.author.data
    og_rating = form.rating.data

    if request.method == "GET":

        form.title.data = book_to_update.title
        form.author.data = book_to_update.author
        form.rating.data = book_to_update.rating
        return render_template("update.html", error=None, form=form, num=num)

    elif request.method == "POST":

        if form.validate_on_submit():
            book_to_update.title = form.title.data.title()
            book_to_update.author = form.author.data.title()
            book_to_update.rating = form.rating.data
            print(f"Title - og: {og_title} --> {book_to_update.title}")
            print(f"Author - og: {og_author} --> {book_to_update.author}")
            print(f"Rating - og: {og_rating} --> {book_to_update.rating}")

            db.session.commit()

            flash("Success! Record Updated.")

            return redirect(url_for("get_book", num=num))

@app.route("/book/<int:num>/delete", methods=["GET", "POST"])
def delete(num):
    book_to_delete = db.session.execute(db.select(Book).where(Book.id == num)).scalar()


    db.session.delete(book_to_delete)
    db.session.commit()

    flash("Success! Record Deleted.")

    return redirect(url_for("home"))



