from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length
from application import T, t

class PostForm(FlaskForm):
    content = TextAreaField(t(T.WRITE), 
                            validators=[DataRequired(), Length(min=1, max=512)])
    submit = SubmitField(t(T.SEND))


class EmptyForm(FlaskForm):
    submit = SubmitField(t(T.ACCEPT))


class MessageForm(FlaskForm):
    message = TextAreaField(t(T.MESSAGE), 
                            validators=[DataRequired(), Length(min=1, max=512)])
    submit = SubmitField(t(T.SEND))

