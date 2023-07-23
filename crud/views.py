# crud 앱의 엔드포인트
from project.crud.forms import UserForm         # 데이터베이스 가져오기
from flask import Blueprint, render_template, redirect, url_for
from project.book import db
from project.crud.models import User
from flask_login import login_required

# blueprint로 crud 앱 생성, 객체화
crud = Blueprint(
    "crud",
    __name__,
    template_folder="templates",
    static_folder="static",
)


# 시작 페이지
@crud.route("/")
def start():
    return render_template("crud/start.html")


# 회원정보
@crud.route("/users")
@login_required
def users():
    users = User.query.all()
    return render_template("crud/index.html", users=users)

# 회원정보 수정,읽기
@crud.route("/users/<user_id>", methods=["GET", "POST"])
@login_required
def edit_user(user_id):
    form = UserForm()

    user = User.query.filter_by(id=user_id).first()     # User 모델을 이용하여 사용자를 취득한다

    # form으로부터 제출된 경우는 사용자를 갱신하여 사용자의 일람 화면으로 리다이렉트한다
    if form.validate_on_submit():
        user.id = form.user_id.data
        user.username = form.username.data
        user.email = form.email.data
        user.password = form.password.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("crud.users"))

    return render_template("crud/edit.html", user=user, form=form)

# 회원정보 삭제
@crud.route("/users/<user_id>/delete", methods=["POST"])
@login_required
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("crud.users"))
