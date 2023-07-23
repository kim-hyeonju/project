from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class UserForm(FlaskForm):
    user_id = StringField(
        "학번",
        validators=[
            DataRequired(message="학번은 필수입니다."),
            Length(max=10, message="학번양식에 맞게 입력해주세요"),
        ],
    )
    username = StringField(
        "사용자명",
        validators=[
            DataRequired(message="사용자명은 필수입니다."),
            Length(max=30, message="30문자 이내로 입력해 주세요"),
        ],
    )

    email = StringField(
        "메일 주소",
        validators=[
            DataRequired(message="메일 주소는 필수입니다."),
            Email(message="메일 주소의 형식으로 입력해주세요"),
        ],
    )

    password = PasswordField(
        "비밀번호",
        validators=[DataRequired(message="비밀번호는 필수입니다.")]
    )

    submit = SubmitField("신규등록")