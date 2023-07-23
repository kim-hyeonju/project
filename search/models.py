from datetime import datetime
from project.book import db


class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    bookname = db.Column(db.String, index=True)
    shelf = db.Column(db.String, index=True)
    block = db.Column(db.String, index=True)
    writer = db.Column(db.String, index=True)
    loan = db.Column(db.String, index=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(
        db.DateTime, default=datetime.now, onupdate=datetime.now
    )
