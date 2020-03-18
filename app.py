# Importing necessary Python libraries
import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json

# Importing objects from other files in this repo
from auth import AuthError, requires_auth
from models import setup_db, Movie, Actor, casting_db


# Defining everything for our Flask application
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    CORS(app, resources={r'/api/': {'origins': '*'}})

    # Instantiating the app with the database from the models file
    setup_db(app)

    # Adding proper header info to response
    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type, Authorization, True')
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET, PATCH, POST, DELETE, OPTIONS')
        return response

    # Default Endpoint
    # -------------------------------------------------------------------------
    @app.route('/', methods=['GET'])
    def check_health():
        return jsonify({
            'success': True,
            'description': 'App is running.'
        })

    # GET Endpoints
    # -------------------------------------------------------------------------

    # Creating an endpoint to view movie information
    @app.route('/movies', methods=['GET'])
    @requires_auth('view:movies')
    def get_movies(jwt):
        # Querying all the movies
        movies = Movie.query.all()

        # Ensuring results are returned else throwing error
        if not movies:
            abort(404)

        # Formatting the returned movie results
        movies = [movie.format() for movie in movies]

        # Returining movie information
        return jsonify({
            'success': True,
            'movies': movies
        })

    # Creating an endpoint to view actor information
    @app.route('/actors', methods=['GET'])
    @requires_auth('view:actors')
    def get_actors(jwt):
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
    @app.route('/movies/create', methods=['POST'])
    @requires_auth('add:movies')
    def add_movie(jwt):
        # Getting information from request body
        body = request.get_json()

        # Extracting information from body
        title = body.get('title')
        release_year = body.get('release_year')

        # Checking to see if proper info is present
        if not (title and release_year):
            abort(422)

        try:
            # Adding new movie object with request body info
            new_movie = Movie(title=title, release_year=release_year)
            new_movie.insert()

            # Returning success information
            return jsonify({
                'success': True,
                'movie_id': new_movie.id,
            })
        except BaseException:
            abort(422)

    # Creating an endpoint to allow a new actor to be added
    @app.route('/actors/create', methods=['POST'])
    @requires_auth('add:actors')
    def add_actor(jwt):
        # Getting information from request body
        body = request.get_json()

        # Extracting information from the body
        name = body.get('name')
        age = body.get('age')
        gender = body.get('gender')
        movie_id = body.get('movie_id')

        # Checking to see if proper info is present
        if not (name and age and gender and movie_id):
            abort(422)

        try:
            # Adding new actor object with request body info
            actor = Actor(name=name,
                          age=age,
                          gender=gender,
                          movie_id=movie_id)
            actor.insert()

            # Returning success information
            return jsonify({
                'success': True,
                'actor_id': actor.id
            })
        except BaseException:
            abort(422)

    # DELETE Endpoints
    # -------------------------------------------------------------------------

    # Creating endpoint to delete a movie by provided movie_id
    @app.route('/movies/delete/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(jwt, movie_id):
        # Querying movie by provided movie_id
        movie = Movie.query.get(movie_id)

        if movie:
            try:
                # Deleting movie from database
                movie.delete()

                # Returning success information
                return jsonify({
                    'success': True,
                    'deleted': movie_id
                })
            except BaseException:
                abort(422)
        else:
            abort(404)

    # Creating endpoint to delete an actor by provided actor_id
    @app.route('/actors/delete/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(jwt, actor_id):
        # Querying actor by provided actor_id
        actor = Actor.query.get(actor_id)

        if actor:
            try:
                # Deleting actor from database
                actor.delete()

                # Returning success information
                return jsonify({
                    'success': True,
                    'deleted': actor_id
                })
            except BaseException:
                abort(422)
        else:
            abort(404)

    # PATCH (Update) Endpoints
    # -------------------------------------------------------------------------

    # Creating an endpoint to update information about a specific movie
    @app.route('/movies/update/<int:movie_id>', methods=['PATCH'])
    @requires_auth('update:movies')
    def update_movie(jwt, movie_id):
        # Querying movie by provided movie_id
        movie = Movie.query.get(movie_id)

        # Checking to see if movie info is present
        if movie:
            try:
                # Getting information from request body
                body = request.get_json()

                # Extracting information from body
                title = body.get('title')
                release_year = body.get('release_year')

                # Updating movie information if new attribute information is
                # present
                if title:
                    movie.title = title
                if release_year:
                    movie.release_year = release_year

                # Updating movie information formally in database
                movie.update()

                # Returning success information
                return jsonify({
                    'success': True,
                    'movie_id': movie.id
                })
            # Raising exception if error updating movie
            except BaseException:
                abort(422)
        # Raising exception if movie could not be found
        else:
            abort(404)

    # Creating an endpoint to update actor information with new attribute info
    @app.route('/actors/update/<int:actor_id>', methods=['PATCH'])
    @requires_auth('update:actors')
    def update_actors(jwt, actor_id):
        # Querying actor by provided actor_id
        actor = Actor.query.get(actor_id)

        # Checking to see if actor info is present
        if actor:
            try:
                # Getting information from request body
                body = request.get_json()

                # Extracting information from body
                name = body.get('name')
                age = body.get('age')
                gender = body.get('gender')
                movie_id = body.get('movie_id')

                # Updating actor information if new attribute information is
                # present
                if name:
                    actor.name = name
                if age:
                    actor.age = age
                if gender:
                    actor.gender = gender
                if movie_id:
                    actor.movie_id = movie_id

                # Updating actor information formally in database
                actor.update()

                # Returning success information
                return jsonify({
                    'success': True,
                    'actor_id': actor.id
                })
            # Raising exception if error updating actor
            except BaseException:
                abort(422)
        # Raising exception if actor could not be found
        else:
            abort(404)

    # Error Handling
    # -------------------------------------------------------------------------
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "not found"
        }), 404

    @app.errorhandler(AuthError)
    def handle_auth_errors(x):
        return jsonify({
            'success': False,
            'error': x.status_code,
            'message': x.error
        }), 401

    return app


# Creating the Flask application
app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
