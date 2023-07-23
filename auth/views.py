from project.book import db
from project.auth.forms import SignUpForm, LoginForm
from project.crud.models import User
from flask_login import login_user, logout_user
from flask import Blueprint, render_template, flash, url_for, redirect, request

auth = Blueprint(
    "auth",
    __name__,
    template_folder="templates",
    static_folder="static"
)

@auth.route("/signup", methods=["GET", "POST"])         #API 만드는 중
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(
            id=form.user_id.data,
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )

        db.session.add(user)
        db.session.commit()

        login_user(user)

        next_ = request.args.get("next")
        if next_ is None or not next_.startswith("/"):
            next_ = url_for("crud.users")
        return redirect(next_)

    return render_template("auth/signup.html", form=form)


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        # 메일 주소로부터 사용자를 취득한다
        user = User.query.filter_by(id=form.user_id.data).first()

        # 사용자가 존재하고 비밀번호가 일치하는 경우는 로그인을 허가한다
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for("search.bookdb"))

        # 로그인 실패 메시지를 설정한다
        flash("메일 주소 또는 비밀번호가 일치하지 않습니다")
    return render_template("auth/login.html", form=form)


@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
