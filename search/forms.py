from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class BooksForm(FlaskForm):
    book_id = StringField(
        "고유번호",
        validators=[
            DataRequired(message="고유번호는 필수입니다."),
            Length(max=5, message="양식에 맞게 입력해주세요"),
        ],
    )
    bookname = StringField(
        "책 제목",
        validators=[
            DataRequired(message="책 제목은 필수입니다."),
            Length(max=30, message="30문자 이내로 입력해 주세요"),
        ],
    )
    shelf = StringField(
        "책장번호",
        validators=[
            DataRequired(message="책장번호 필수입니다."),
            Length(max=30, message="30문자 이내로 입력해 주세요"),
        ],
    )
    block = StringField(
        "블록",
        validators=[
            DataRequired(message="블록은 필수입니다."),
            Length(max=30, message="30문자 이내로 입력해 주세요"),
        ],
    )
    writer = StringField(
        "작가",

    )
    loan = StringField(
        "대출여부",        
        validators=[
            DataRequired(message="작가명은 필수입니다."),
            Length(max=30, message="30문자 이내로 입력해 주세요"),
        ],
    )

    submit = SubmitField("등록")
