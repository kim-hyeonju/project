from pathlib import Path
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager

db = SQLAlchemy()               # SQLAlchemy 인스턴스화
csrf = CSRFProtect()
login_manager = LoginManager()


login_manager.login_view = "auth.signup"
login_manager.login_message = ""


def create_app():               # flask앱 생성하는 함수
    app = Flask(__name__)

    app.config.from_mapping(                                # SQLite을 SQLAlchemy로 사용하기위해 입의 config 설정
        SECRET_KEY="2AZSMss3p5QPbcY2hBsJ",
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}",       # SQLit의 데이터베이스 출력하는 경로 지정
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_ECHO=True,            # SQL을 콘솔로그에 출력
        WTF_CSRF_SECRET_KEY="Ausdkldgklsdf"
    )

    csrf.init_app(app)
    db.init_app(app)                # SQLAlchemy 와 앱을 연계
    login_manager.init_app(app)
    Migrate(app, db)

    from project.crud import views as crud_views
    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    from project.auth import views as auth_views
    app.register_blueprint(auth_views.auth, url_prefix="/auth")

    from project.search import views as search_views
    app.register_blueprint(search_views.search, url_prefix="/search")

    return app
