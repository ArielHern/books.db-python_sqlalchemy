from flask import Flask, render_template, request

from config import DATABASE_URI
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


def main():
    books = Book.query.all()
    for book in books:
        print(f"{book.title}")


if __name__ == "__main__":
    with app.app_context():
        main()
