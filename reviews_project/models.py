from werkzeug.security import generate_password_hash #generates a unique password hash for extra security 
from flask_sqlalchemy import SQLAlchemy #this is our ORM (Object Relational Mapper)
from flask_login import UserMixin, LoginManager #helping us load a user as our current_user 
from datetime import datetime #put a timestamp on any data we create (Users, Products, etc)
import uuid #makes a unique id for our data (primary key)
from flask_marshmallow import Marshmallow

#internal imports
from .helpers import get_image, get_movie_details


#instantiate all our classes
db = SQLAlchemy() #make database object
login_manager = LoginManager() #makes login object 
ma = Marshmallow()

#use login_manager object to create a user_loader function
@login_manager.user_loader
def load_user(user_id):
    """Given *user_id*, return the associated User object.

    :param unicode user_id: user_id (email) user to retrieve

    """
    return User.query.get(user_id) #this is a basic query inside our database to bring back a specific User object

#think of these as admin (keeping track of what products are available to sell)
class User(db.Model, UserMixin): 
    #CREATE TABLE User, all the columns we create
    user_id = db.Column(db.String, primary_key=True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow) #this is going to grab a timestamp as soon as a User object is instantiated


    #INSERT INTO User() Values()
    def __init__(self, username, email, password, first_name="", last_name=""):
        self.user_id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email 
        self.password = self.set_password(password) 



    #methods for editting our attributes 
    def set_id(self):
        return str(uuid.uuid4()) #all this is doing is creating a unique identification token
    

    def get_id(self):
        return str(self.user_id) #UserMixin using this method to grab the user_id on the object logged in
    
    
    def set_password(self, password):
        return generate_password_hash(password) #hashes the password so it is secure (aka no one can see it)
    

    def __repr__(self):
        return f"<User: {self.username}>"
    
class MovieReview(db.Model):
    review_id = db.Column(db.String, primary_key=True)
    movie_title = db.Column(db.String(100), nullable=False)
    review_text = db.Column(db.String(1000))
    rating = db.Column(db.Numeric(precision=2, scale=1), nullable=False)
    reviewer_name = db.Column(db.String(50), nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    movie_director = db.Column(db.String(100))
    movie_year = db.Column(db.String(4))
    movie_plot = db.Column(db.String(1000))
    movie_poster = db.Column(db.String)

    def __init__(self, movie_title, reviewer_name, rating, review_text=""):
        self.review_id = self.set_id()
        self.movie_title = movie_title
        self.review_text = review_text
        self.rating = rating
        self.reviewer_name = reviewer_name
        movie_details = get_movie_details(movie_title)
        if movie_details != "Movie not found.":
            self.movie_director = movie_details.get('director')
            self.movie_year = movie_details.get('year')
            self.movie_plot = movie_details.get('plot')
        self.movie_poster = get_image(movie_title)

    def set_id(self):
        return str(uuid.uuid4())

    def __repr__(self):
        return f"<MovieReview '{self.movie_title}' by {self.reviewer_name}>"


class MovieReviewSchema(ma.Schema):
    class Meta:
        fields = ['review_id', 'movie_title', 'review_text', 'rating', 'reviewer_name', 'date_posted']

# Instantiate the MovieReviewSchema
movie_review_schema = MovieReviewSchema()  # For a single movie review
movie_reviews_schema = MovieReviewSchema(many=True)  # For multiple movie reviews
