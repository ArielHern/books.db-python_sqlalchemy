import csv

from flask import Flask, render_template, request

from config import DATABASE_URI
from models import *

app = Flask(__name__)  # flask app
# postgress string from config.py
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


def main():
    # Open the book.csv  creates a new book from each object book"""
    f = open("books.csv", encoding='utf-8')
    reader = csv.reader(f)
    next(reader)
    for title, author, average_rating, isbn, lenguague_code, pages in reader:
        book = Book(title=title, author=author, average_rating=average_rating,
                    isbn=isbn, lenguague_code=lenguague_code, pages=pages)
        db.session.add(book)

    db.session.commit()  # commits to the db


if __name__ == "__main__":
    with app.app_context():
        main()
