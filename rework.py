from app import app

if __name__ == "__main__":
    app.run(debug=True)


"""
NOTE TO SELF: 8/5/24
- app.context needs to be tweaked, not creating new books table (and thus not saving to db)
- add validation to search db for titles to verify no duplicate before commit
"""