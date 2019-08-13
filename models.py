### models.py ###

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Book(db.Model):
    """Book table with autoincrememt id,
    title, author, ave_rating, isbn, lenguague, #_pages"""
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    author = db.Column(db.String)
    average_rating = db.Column(db.String)
    isbn = db.Column(db.String)
    lenguague_code = db.Column(db.String)
    pages = db.Column(db.Integer)
