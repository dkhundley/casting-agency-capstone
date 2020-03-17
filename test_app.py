# Importing the necessary libraries
import os
import unittest
import json
import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# Importing objects from other files in the repo
from models import Actor, Movie, setup_db, casting_db
from app import create_app

# Creating a Unit Test class object to hold all our unit tests
class CastingTestCase(unittest.TestCase):
    # Establishing function to initialize items to perform tests
    def setup_for_tests(self):
        self.app = create_app()
        self.client = self.app.test_client
        setup_db(self.app)
        casting_db.drop_all()
        casting_db.create_all()

        self.test_movie = {
            'title': 'Some Movie Title',
            'release_date': datetime.date(2020, 3, 17)
        }

        self.test_actor = {
            'name': 'Jane Doe',
            'age': 22,
            'gender': 'female',
            'movie_id': '1'
        }

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
