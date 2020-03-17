# Importing necessary Python libraries
import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Importing objects from other files in this repo
from auth import AuthError, requires_auth
from models import setup_db, Movie, Actor, casting_db

# Defining everything for our Flask application
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    CORS(app, resources = {r"/api/": {"origins": "*"}})

    # Instantiating the app with the database from the models file
    setup_db(app)

    # GET Endpoints
    # -------------------------------------------------------------------------

    # Creating an endpoint to view movie information
    @app.route('/movies', methods = ['GET'])
    @requires_auth('view:movies')
    def get_movies():
        # Querying all the movies
        movies = Movie.query.all()

        # Ensuring results are returned else throwing error
        if not movies:
          abort(404)

        # Formatting the returned movie results
        movies = [movie.format() for movie in movies]

        # Formatting the actors field within movies
        for movie in movies:
          movie['actor'] = [actor.format() for actor in movie['actors']]

        # Returining movie information
        return jsonify({
          'success': True,
          'movies': movies
        })

    # Creating an endpoint to view actor information
    @app.route('/actors', methods = ['GET'])
    @requires_auth('view:actors')
    def get_actors():
        # Querying all the actors
        actors = Actor.query.all()

        # Ensuring results are returned else throwing error
        if not actors:
          abort(404)

        # Formatting the return actor results
        actors = [actor.format() for actor in actors]

        # Returning actor information
        return jsonify({
            'success': True,
            'actors': actors
        })

    # POST Endpoints
    # -------------------------------------------------------------------------

    # Creating an endpoint to allow a new movie to be added
    @app.route('/movies/create', methods = ['POST'])
    @requires_auth('add:movies')
    def add_movie():
        # Getting information from request body
        body = request.get_json()

        # Checking to see if proper info is present
        if not ('title' in body and 'release_date' in body):
            abort(422)

        # Extracting information from body
        title = body.get('title')
        release_date = body.get('release_date')

        try:
            # Adding new movie object with request body info
            movie = Movie(title = title, release_date = release_date)
            movie.insert()

            # Returning success information
            return jsonify({
                'success': True,
                'movie_id': movie.id,
            })
        except:
            abort(422)

    # Creating an endpoint to allow a new actor to be added
    @app.route('/actors/create', methods = ['POST'])
    @requires_auth('add:actors')
    def add_actor():
        # Getting information from request body
        body = request.get_json()

        # Checking to see if proper info is present
        if not ('name' in body and 'age' in body and 'gender' in body and 'movie_id' in body):
            abort(422)

        # Extracting information from the body
        name = body.get('name')
        age = body.get('age')
        gender = body.get('gender')
        movie_id = body.get('movie_id')

        try:
            # Adding new actor object with request body info
            actor = Actor(name = name,
                          age = age,
                          gender = gender,
                          movie_id = movie_id)
            actor.insert()

            # Returning success information
            return jsonify({
                'success': True,
                'actor_id': actor.id
            })
        except:
            abort(422)


    return app

# Creating the Flask application
APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
