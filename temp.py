@app.route("/update/<target_id>", methods=["GET", "POST"])
def update(target_id):
    book_to_update = db.session.execute(db.select(Book).where(Book.id == target_id)).scalar()
    form = BookForm(obj=book_to_update)
    current_title = form.title.data
    record_id = book_to_update.id
    print(f"current b4 if: {current_title}")
    print(f"b4 if id: {record_id}")
    # if request.method == "POST":
    if form.validate_on_submit():
        form.populate_obj(book_to_update)
        update_title = form.title.data.title()
        update_author = form.author.data.title()
        update_rating = form.author.data.title()
        print(f"current title: {current_title}")
        print(f"update: {update_title}")
        print(f"update auth: {update_author}")
        print(f"update rating: {update_rating}")

            # if current_title != update_title:
            #
            #     # Check for title
            #     title_check = validate_title(update_title)
            #
            #     if title_check is None:
            #         print("Title verified")
            #         print(f"title_check: {title_check}")
            #
            #         db.session.add(book_to_update)
            #         db.session.commit()
            #         return redirect(url_for('home'))

    return render_template("update.html", error=None, form=form)