# Importing the necessary libraries
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# Importing objects from other files in the repo
from models import Actor, Movie, setup_db
from app import create_app

# Creating a Unit Test class object to hold all our unit tests
class CastingTestCase(unittest.TestCase):
    # Establishing function to initialize items to perform tests
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        setup_db(self.app)

        self.test_movie = {
            'title': 'Some Movie Title',
            'release_year': 2020
        }

        self.test_actor = {
            'name': 'Jane Doe',
            'age': 22,
            'gender': 'female',
            'movie_id': 1
        }

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.drop_all()
            self.db.create_all()

    # Passing over teardown
    def tearDown(self):
        pass

    # GET Endpoint Tests
    # -------------------------------------------------------------------------

    # Creating a test for the /movies GET endpoint
    def test_get_movies(self):
        # Retrieving information from endpoint
        res = self.client().get('/movies')
        # Transforming body response into JSON
        data = json.loads(res.data)

        # Asserting that tests are valid
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    # Creating a test to ensure a proper error is thrown if incorrect /movies endpoint is called
    def test_get_movies_fail(self):
        # Retriving information from the endpoint
        res = self.client().get('/moovies')
        # Transforming body response into JSON
        data = json.loads(res.data)

        # Asserting that tests are valid
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'not found')

    # Creating a test for the /acotrs GET endpoint
    def test_get_actors(self):
        # Retrieving information from endpoint
        res = self.client().get('/actors')
        # Transforming body response into JSON
        data = json.loads(res.data)

        # Asserting that tests are valid
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    # Creating a test to ensure a proper error is thrown if incorrect /actors endpoint is called
    def test_get_actors_fail(self):
        # Retriving information from the endpoint
        res = self.client().get('/acters')
        # Transforming body response into JSON
        data = json.loads(res.data)

        # Asserting that tests are valid
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'not found')

    # POST Endpoint Tests
    # -------------------------------------------------------------------------

    # Creating a test for the /movies/create POST endpoint
    def test_add_movie(self):
        # Posting dummy movie data to movies POST endpoint
        res = self.client().post('/movies/create', json = self.test_movie)
        # Transforming body response into JSON
        data = json.loads(res.data)

        # Asserting that tests are valid
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie_id'])

    # Creating a test to throw proper error if /movies/create endpoint not called correctly
    def test_add_movie_fail(self):
        # Posting incomplete dummy movie data to the movies POST endpoint
        res = self.client().post('/movies/create', json = {'title': 'Movie Title'})
        # Transforming body response into JSON
        data = json.loads(res.data)

        # Asserting that tests are valid
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 422)
        self.assertEqual(data['message'], 'unprocessable')

    # Creating a test for the /actors/create POST endpoint
    def test_add_actor(self):
        # Posting dummy actor data to movies POST endpoint
        res = self.client().post('/actors/create', json = self.test_actor)
        # Transforming body response into JSON
        data = json.loads(res.data)

        # Asserting that tests are valid
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor_id'])

    # Creating a test to throw proper error if /actors/create endpoint not called correctly
    def test_add_actor_fail(self):
        # Posting incomplete dummy actor data to the movies POST endpoint
        res = self.client().post('/actors/create', json = {'name': 'John Doe'})
        # Transforming body response into JSON
        data = json.loads(res.data)

        # Asserting that tests are valid
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 422)
        self.assertEqual(data['message'], 'unprocessable')

    # DELETE Endpoint Tests
    # -------------------------------------------------------------------------

    # Creating a test to delete a movie using the DELETE endpoint
    def test_delete_movie(self):
        # Calling delete endpoint with valid movie_id
        res = self.client().delete('/movies/delete/2')
        # Transforming body response into JSON
        data = json.loads(res.data)

        # Asserting that tests are valid
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted'])

    # Creating a test to verify correct error is thrown when invalid movie_id is passed to delete endpoint
    def test_delete_movie_fail(self):
        # Calling delete endpoint with invalid movie_id
        res = self.client().delete('/movies/delete/100000000')
        # Transforming body response into JSON
        data = json.loads(res.data)

        # Asserting that tests are valid
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'not found')

    # Creating a test to delete an actor using the DELETE endpoint
    def test_delete_actor(self):
        # Calling delete endpoint with valid actur_id
        res = self.client().delete('/actors/delete/1')
        # Transforming body response into JSON
        data = json.loads(res.data)

        # Asserting that tests are valid
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted'])

    # Creating a test to verify correct error is thrown when invalid actor_id is passed to delete endpoint
    def test_delete_actor_fail(self):
        # Calling delete endpoint with invalid actor_id
        res = self.client().delete('/actors/delete/100000000')
        # Transforming body response into JSON
        data = json.loads(res.data)

        # Asserting that tests are valid
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'not found')

    # PATCH (Update) Endpoint Tests
    # -------------------------------------------------------------------------

    # Creating a test to update a movie with new info
    def test_update_movie(self):
        # Calling patch endpoint with valid movie_id
        res = self.client().patch('/movies/update/3', json = {'title': 'Updated movie title'})
        # Transforming body response into JSON
        data = json.loads(res.data)

        # Asserting that tests are valid
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie_id'])

    # Creating a test to throw proper error when invalid movie_id is passed to PATCH endpoint
    def test_update_movie_fail(self):
        # Calling patch endpoint with invalid movie_id
        res = self.client().patch('/movies/update/100000000', json = {'title': 'Updated movie title'})
        # Transforming body response into JSON
        data = json.loads(res.data)

        # Asserting that tests are valid
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'not found')

    # Creating a test to update an actor with new info
    def test_update_actor(self):
        # Calling patch endpoint with valid actor_id
        res = self.client().patch('/actors/update/2', json = {'name': 'Updated Name'})
        # Transforming body response into JSON
        data = json.loads(res.data)

        # Asserting that tests are valid
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor_id'])

    # Creating a test to throw proper error when invalid actor_id is passed to PATCH endpoint
    def test_update_actor_fail(self):
        # Calling patch endpoint with invalid actor_id
        res = self.client().patch('/actors/update/100000000', json = {'name': 'Updated Name'})
        # Transforming body response into JSON
        data = json.loads(res.data)

        # Asserting that tests are valid
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'not found')


# Make the tests conveniently executable
if __name__ == '__main__':
    unittest.main()
