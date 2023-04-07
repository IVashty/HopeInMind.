from wtforms import (
    StringField,
    PasswordField,
    BooleanField,
    IntegerField,
    DateField,
    TextAreaField,
)
from flask_wtf import FlaskForm
from wtforms.validators import (
    InputRequired,
    Length,
    EqualTo,
    Email,
    Regexp,
    Optional,
)
from flask_login import current_user
from wtforms import ValidationError, validators
from models import User
import email_validator


# Define the login form
class LoginForm(FlaskForm):
    """
    Login form that extends FlaskForm.
    """

    email = StringField(validators=[InputRequired(), Email(), Length(1, 64)])
    pwd = PasswordField(validators=[InputRequired(), Length(min=8, max=72)])
    # Placeholder labels to enable form rendering
    username = StringField(validators=[Optional()])


# Define the register form
class RegisterForm(FlaskForm):
    """
    Registration form that extends FlaskForm.
    """

    username = StringField(
        validators=[
            InputRequired(),
            Length(3, 20, message="Please provide a valid name"),
            Regexp(
                "^[A-Za-z][A-Za-z0-9_.]*$",
                0,
                "Usernames must have only letters, numbers, dots or underscores",
            ),
        ]
    )
    email = StringField(validators=[InputRequired(), Email(), Length(1, 64)])
    pwd = PasswordField(validators=[InputRequired(), Length(8, 72)])
    cpwd = PasswordField(
        validators=[
            InputRequired(),
            Length(8, 72),
            EqualTo("pwd", message="Passwords must match!"),
        ]
    )

    def validate_email(self, email):
        """
        Validate if the email is already registered in the database.
        """
        if User.query.filter_by(email=email.data).first():
            raise ValidationError("Email already registered!")

    def validate_username(self, username):
        """
        Validate if the username is already taken in the database.
        """
        if User.query.filter_by(username=username.data).first():
            raise ValidationError("Username already taken!")
