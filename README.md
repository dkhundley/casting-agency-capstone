# Casting Agency Capstone Project
This project is my capstone project for the Udacity Full Stack Nanodegree. In it, we'll be leveraging several different pieces of technology to create web-hosted API with a database backend. The nature of this API has to do with movie casting. As we'll cover more down below, the API will cover pieces surrounding actors / actresses and their respective movies.

## Getting Started
The application itself is hosted on the Heroku platform. You can navigate to it at this link: [https://casting-api.herokuapp.com](https://casting-api.herokuapp.com).

If you navigate to the app in the browser, you will be greeted with a basic message noting that the app is indeed up and running. In order to actually use this app, you will need to be authenticated with my Auth0 domain. We'll cover more in another section how you as a Udacity reviewer might interact with this with some pre-generated tokens via Postman.

## Tech Stack
To give you a flavor on how this API was put together and deployed, we'll cover some of the pieces of the tech stack here:

- **Heroku**: This is the platform where this Git repository was pushed to and built from. It leverages the ```requirements.txt``` file to install the necessary Python libraries, ```Procfile``` to start up the Gunicorn web server, and ```manage.py``` to leverage Flask Migrate to build the PostGres database models.
- **Auth0**: Auth0 is the service we'll be using for proper authentication and authorization. We'll cover off more how this is specifically being used in another section.
- **Flask**: Flask and it's respective counterparts are what we are using to build this API in Python code. This particular Flask application contains several endpoints for various aspects of the casting API, and we'll cover that more in a future section.
- **Postman**: This isn't doing anything to enable the application itself, but it helps us with testing to ensure everything is working properly. (Additionally, there is a ```test_app.py``` file that was performed to verify unit testing.)

## Data Models

Before moving into how the API functions, it is good to know the data models supporting the API behind the scenes. In this project, we have two data models: **actors** and **movies**. The following subsections go into more details about the respective attributes of each of those models.

### Movies
- **id**: Auto-incrementing integer value
- **title**: String value
- **release_year**: Integer value

### Actors
- **id**: Auto-incrementing integer value
- **name**: String value
- **age**: Integer value
- **gender**: String value
- **movie_id**: Integer value that denotes foreign key relationship to ```id``` field in ```movies``` table

## Auth0 Roles, Permissions, and More

Within Auth0, we have established 3 high level roles and have associated different permissions for each role. Each role is progressive in the sense that a "higher" level role inherits all the permissions from a lower level one.

Here are the roles and permissions as defined in Auth0:
- **Casting Assistant**: This lowest level role only has basic view capabilities. Permissions include...
  - ```view:movies```
  - ```view:actors```
- **Casting Director**: As our middle tier role, this role inherits the same permissions from the Casting Assistant role as well as adds some additional permissions. These include...
  - ```add:movies```
  - ```add:actors```
  - ```update:movies```
  - ```update:actors```
- **Executive Producer**: Finally, our highest tier role contains all permissions from the roles already defined above as well as gains a few new permissions around deleting resources. These specific permissions are...
  - ```delete:movies```
  - ```delele:actors```

### Auth0 Account Setup
If you would like to setup your own account with my Auth0 instance, you can do so at the URL below. However, please note that this isn't much good for you unless add one of the respective roles above to your account. (I'm not sure how to do this in an automated fashion; this seems out of scope for this project.)

Auth0 URL: [https://dkhundley.auth0.com/authorize?audience=casting&response_type=token&client_id=XsFZ8sZs1c56mZz1Wfnjc2g7Epd8bIV2&redirect_uri=http://127.0.0.1:8080/login-results](https://dkhundley.auth0.com/authorize?audience=casting&response_type=token&client_id=XsFZ8sZs1c56mZz1Wfnjc2g7Epd8bIV2&redirect_uri=http://127.0.0.1:8080/login-results)

### Active Tokens
As of today (3/18/2020), I have generated a handful of tokens associated to each of the roles mentioned above. These tokens are also included in the Postman documentation and should be valid for the next few days. These tokens are as followed:
  - **Casting Assistant Token**: ```eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJEZ3pNemd5TlRkRk5EWkdSakZHTVVNMk4wUTBNREF5TlVKQ1JrVXhSRU16UVRBNU9EbEdRZyJ9.eyJpc3MiOiJodHRwczovL2RraHVuZGxleS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU3MjBkNTUyNjFiZjQwY2FkNTk0ODFiIiwiYXVkIjoiY2FzdGluZyIsImlhdCI6MTU4NDUzNzc3NSwiZXhwIjoxNTg0NTQ0OTc1LCJhenAiOiJYc0ZaOHNaczFjNTZtWnoxV2ZuamMyZzdFcGQ4YklWMiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsidmlldzphY3RvcnMiLCJ2aWV3Om1vdmllcyJdfQ.RHrBlrYQGIzEPokrbRGoQ08gTg_p8Kf9aAsWcivLzPGYR6oFfYyaXs5gohizqwPKBFaMbfPQdysJA7_V-IKI6EfE5HwvHbArqGVO1B3q5b0RI6CLsIdaEfI04XO8MURqm7c_xyE2vFLOtpc2-dv7QfIwCmqdiFjnymh29Lk_-Wgl-pDK0QzRa7EEtny62Eq4gvUxNbdf5BX1zK2HL0mDM7pRWv1mJVvoDsSnB03FfarbQZrxP1lfm9_TXDKEJoYboqrqAqYVr-wEuv_mG6NVYteIvm4WDbzMbbZI6ckFVJKLjhUm93jiNNEyTeNQaqzRLOH726Gccjpd3PlC18iqZg```
  - **Casting Director Token**: ```eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJEZ3pNemd5TlRkRk5EWkdSakZHTVVNMk4wUTBNREF5TlVKQ1JrVXhSRU16UVRBNU9EbEdRZyJ9.eyJpc3MiOiJodHRwczovL2RraHVuZGxleS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU2YmEyMjIxM2U2ZjAwY2I1NjNiZWNmIiwiYXVkIjoiY2FzdGluZyIsImlhdCI6MTU4NDUzNDgyNSwiZXhwIjoxNTg0NTQyMDI1LCJhenAiOiJYc0ZaOHNaczFjNTZtWnoxV2ZuamMyZzdFcGQ4YklWMiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiYWRkOmFjdG9ycyIsImFkZDptb3ZpZXMiLCJ1cGRhdGU6YWN0b3JzIiwidXBkYXRlOm1vdmllcyIsInZpZXc6YWN0b3JzIiwidmlldzptb3ZpZXMiXX0.GZpXVw8lWvlQSa2KF7skn26gplwzbo7kC3AahXAuOuNR7WhZzUWAEMxN-IeBZv2wB06-zmDLE6RexwXjKRkS3vACJRYj1Cq-6YcjCTwENDKXGEWq9I9rxr1ZNag7cr7xz897T6BOFK8wMQja7u6KkzUw0wn_khOHSE47jAFu15JgV0m6e8PJwdGmDw46r3azkcNCRAUsh6_1F__7orKaqAzAmI26PjS_M2xBG_ThSrrnW-66X9jssBJgHN5j8cWGVSDehue3gMzrUa5hphC6hJ3-1h2MuxmTvZZ3W50SMDZRde9-fOIIK_jW-xHheHsr-qxqn5iITM-Fi3Tnc3wH2g```
  - **Executive Producer Token**: ```eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJEZ3pNemd5TlRkRk5EWkdSakZHTVVNMk4wUTBNREF5TlVKQ1JrVXhSRU16UVRBNU9EbEdRZyJ9.eyJpc3MiOiJodHRwczovL2RraHVuZGxleS5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDUwNTU1OTY4NzQ1NDA2MzkxNjMiLCJhdWQiOlsiY2FzdGluZyIsImh0dHBzOi8vZGtodW5kbGV5LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1ODQ1NDA5NDgsImV4cCI6MTU4NDYyNzM0OCwiYXpwIjoiWHNGWjhzWnMxYzU2bVp6MVdmbmpjMmc3RXBkOGJJVjIiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiYWRkOmFjdG9ycyIsImFkZDptb3ZpZXMiLCJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsInVwZGF0ZTphY3RvcnMiLCJ1cGRhdGU6bW92aWVzIiwidmlldzphY3RvcnMiLCJ2aWV3Om1vdmllcyJdfQ.N6tiQOU0R71M752oxyx9cFiovZ7BkedP49l573qlo_jQJeoF0TP17AFz00tL-qJOroTUErHiBGc7CTGantx7Jg6vgWYTbdVjMYt6Kufg5kO-y2agjm2InfHXdD2ZU8KeSxeIY_o1yAqe9J9gbXXKpc9DC1ouEMq1MSY1Sju9t2xDlOmcECgVDGQ4q5oWNfQ8b9MuvmICbV8BKcxvgjDPL8Ol_J5Uu5FcXMHaJ64UFvJxPS9UwOwr-zQpJV_V-SKKK3jYTIgDg2nrlJUE_Xx3ejwcKbzp2vVspzl-WK5UZ4Lm-6d5HTqwx3KGisEdgW-iBqJDY-7cLx7xVJ0aLrHYUA```


## API Endpoints

In the next few subsections, we'll cover how the API works and what you can expect back in the results.

### Default Path

#### GET /
Verifies that application is up and running on Heroku.

Sample response:
```
{
    "description": "App is running.",
    "success": true
}
```

### GET Endpoints

#### GET /movies
Displays all movies listed in the database.

Sample response:
```
{
    "movies": [
        {
            "id": 3,
            "release_year": 2008,
            "title": "Movie 3"
        },
        {
            "id": 4,
            "release_year": 1973,
            "title": "Movie 4"
        },
    ],
    "success": true
}
```

#### GET /actors
Displays all actors / actresses listed in the database.

Sample response:
```
{
    "actors": [
        {
            "age": 34,
            "gender": "female",
            "id": 3,
            "movie_id": 2,
            "name": "Actor 3"
        },
        {
            "age": 34,
            "gender": "male",
            "id": 4,
            "movie_id": 3,
            "name": "Actor 4"
        },
    ],
    "success": true
}
```

### POST Endpoints

#### POST /movies/create
Creates a new movie entry in the database.

Sample response:
```
{
    "movie_id": 8,
    "success": true
}
```

#### POST /actors/create
Creates a new actor / actress entry in the database.

Sample response:
```
{
    "actor_id": 7,
    "success": true
}
```

### PATCH Endpoints

#### PATCH /movies/update/<movie_id>
Updates movie information given a movie_id and newly updated attribute info.

Sample response:
```
{
    "movie_id": 2,
    "success": true
}
```

#### PATCH /actors/update/<actor_id>
Updates actor information given a actor_id and newly updated attribute info.

Sample response:
```
{
    "actor_id": 2,
    "success": true
}
```

### DELETE Endpoints

#### DELETE /movies/delete/<movie_id>
Deletes a movie entry from the database given the inputted movie_id.

Sample response:
```
{
    "deleted": 1,
    "success": true
}
```

#### DELETE /movies/actors/<actor_id>
Deletes an actor / actress entry from the database given the inputted actor_id.

Sample response:
```
{
    "deleted": 1,
    "success": true
}
```
