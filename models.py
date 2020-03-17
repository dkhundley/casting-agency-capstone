# Importing the necessary libraries
import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy

database_name = "casting_test"
database_path = "postgres://{}/{}".format('localhost:5432', database_name)

# Instantiating database as an SQLAlchemy object
casting_db = SQLAlchemy()

# Setting up the database for the Flask app
def setup_db(app, database_path = database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    casting_db.app = app
    casting_db.init_app(app)

# Creating a Movie class object to hold / update information about movies
class Movie(casting_db.Model):
    # Setting the name of the table
    __tablename__ = 'movies'

    # Setting attributes of the table
    id = Column(Integer(), primary_key = True)
    title = Column(String())
    release_year = Column(Integer())

    # Connecting actors from the 'actors' table to the respective movie
    actors = casting_db.relationship('Actor', backref = 'movies')

    # Creating an insert function
    def insert(self):
        casting_db.session.add(self)
        casting_db.session.commit()

    # Creating an update function
    def update(self):
        casting_db.session.commit()

    # Creating a delete function
    def delete(self):
        casting_db.session.delete(self)
        casting_db.session.commit()

    # Creating a formatting function
    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_year': self.release_year
        }

# Creating an Actor class object to hold / update information about actors & actresses
class Actor(casting_db.Model):
    # Setting the name of the table
    __tablename__ = 'actors'

    # Setting the attributes of the table
    id = Column(Integer(), primary_key = True)
    name = Column(String())
    age = Column(Integer())
    gender = Column(String())

    # Connecting movie to the respective actors from the movies table
    movie_id = casting_db.Column(casting_db.Integer, casting_db.ForeignKey('movies.id'), nullable = False)

    # Creating an insert function
    def insert(self):
        casting_db.session.add(self)
        casting_db.session.commit()

    # Creating an update function
    def update(self):
        casting_db.session.commit()

    # Creating a delete function
    def delete(self):
        casting_db.session.delete(self)
        casting_db.session.commit()

    # Creating a formatting function
    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'movie_id': self.movie_id
        }
