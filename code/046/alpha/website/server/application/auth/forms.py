from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, EqualTo, Length
from application import t, T
from application.models import User


class LoginForm(FlaskForm):
    username = StringField(t(T.USER), validators=[DataRequired()])
    password = PasswordField(t(T.PASSWORD), validators=[DataRequired()])
    submit = SubmitField(t(T.SEND))


class RegistrationForm(FlaskForm):
    username = StringField(t(T.USER), validators=[DataRequired()])
    password = PasswordField(t(T.PASSWORD), 
                             validators=[DataRequired()])
    repeat_password = PasswordField(t(T.REPEAT_PASSWORD), 
                                    validators=[DataRequired(), 
                                                EqualTo('password')])
    about_me = StringField(t(T.ABOUT_ME), 
                           validators=[DataRequired(), 
                                       Length(min=10, 
                                              max=32, 
                                              message=t(T.BETWEEN_10_to_32_CHARACTERS))])    
    submit = SubmitField(t(T.REGISTER))

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(t(T.DIFFERENT_USERNAME))

