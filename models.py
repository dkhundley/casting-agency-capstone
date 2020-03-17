# Importing the necessary libraries
import os
from flask_sqlalchemy import SQLAlchemy

# Instantiating database as an SQLAlchemy object
casting_db = SQLAlchemy()

# Setting up the database for the Flask app
def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ['DATABASE_URL']
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    casting_db.app = app
    casting_db.init_app(app)

# Creating a Movies class object to hold / update information about movies
class Movie(casting_db.Model):
    # Setting the name of the table
    __tablename__ = 'movies'

    # Setting attributes of the table
    id = casting_db.Column(casting_db.Integer, primary_key = True)
    title = casting_db.Column(casting_db.String)
    release_date = db.Column(db.Date)

    # Connecting actors from the 'actors' table to the respective movie
    actors = db.relationship('Actor', backref = 'movies')

    # Creating an insert function
    def insert(self):
        casting_db.session.add(self)
        casting_db.session.commit(self)

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
            'release_date': self.release_date,
            'actors': self.actors
        }
