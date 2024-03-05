from operator import length_hint
from tarfile import LENGTH_LINK, LENGTH_NAME
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, IntegerField, DecimalField, SubmitField, TextAreaField 
from wtforms.validators import DataRequired, Email, EqualTo, NumberRange

#creating our login & register forms 
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[ DataRequired(), Email()])
    password = PasswordField('Password', validators=[ DataRequired() ])
    submit = SubmitField('Sign In')


class RegisterForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    username = StringField('Username', validators=[ DataRequired() ])
    email = StringField('Email', validators= [ DataRequired(), Email()])
    password = PasswordField('Password', validators = [ DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[ DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class MovieReviewForm(FlaskForm):
    movie_title = StringField('Movie Title', validators=[DataRequired()])
    review_text = TextAreaField('Review Text **Optional')
    rating = DecimalField('Rating', validators=[DataRequired(), NumberRange(min=0, max=10)], places=1, rounding=None)
    reviewer_name = StringField('Reviewer Name', validators=[DataRequired()])
    submit = SubmitField('Submit Review')