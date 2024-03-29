from flask import Flask, render_template, request
from models import *

from config import DATABASE_URI

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


def main():
    db.drop_all()
    db.create_all()


if __name__ == "__main__":
    with app.app_context():
        main()
