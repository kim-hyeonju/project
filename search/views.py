from project.book import db
from project.search.models import Book
from project.search.forms import BooksForm
from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required

search = Blueprint(
    "search",
    __name__,
    template_folder="templates",
    static_folder="static"
)


# 예시
@search.route("/book")
def index():
    return render_template("search/create.html")


# 데이터베이스 열람
@search.route("/bookdb")
@login_required
def bookdb():
    books = Book.query.all()
    return render_template("search/index.html", books=books)


@search.route("/bookdb/new", methods=["GET", "POST"])
def create_book():
    # UserForm을 인스턴스화한다
    form2 = BooksForm()

    if form2.validate_on_submit():
        # 사용자를 작성한다
        book = Book(
            id=form2.book_id.data,
            bookname=form2.bookname.data,
            shelf=form2.shelf.data,
            block=form2.block.data,
            writer=form2.writer.data,
            loan=form2.loan.data,
        )

        # 사용자를 추가하고 커밋한다
        db.session.add(book)
        db.session.commit()

        # 사용자 데이터베이스 화면으로 리다이렉트한다
        return redirect(url_for("search.bookdb"))
    return render_template("search/create.html", form2=form2)


@search.route("/bookdb/<book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    form = BooksForm()

    # User 모델을 이용하여 사용자를 취득한다
    book = Book.query.filter_by(id=book_id).first()

    # form으로부터 제출된 경우는 사용자를 갱신하여 사용자의 일람 화면으로 리다이렉트한다
    if form.validate_on_submit():
        book.id = form.book_id.data
        book.username = form.bookname.data
        book.shelf = form.shelf.data
        book.block = form.block.data
        book.writer = form.writer.data
        book.loan = form.loan.data
        db.session.add(book)
        db.session.commit()
        return redirect(url_for("search.bookdb"))

    # GET :  HTML을 반환
    return render_template("search/edit.html", book=book, form=form)


@search.route("/bookdb/<book_id>/delete", methods=["POST"])
@login_required
def delete_book(id):
    book = Book.query.filter_by(id=book_id).first()
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("search.bookdb"))
