from models import Actor, Movie
# Creating new function to create a handful of dummy test entries


def db_test_records():
    movie_1 = (Movie(
        title='Movie 1',
        release_year=2020
    ))

    movie_2 = (Movie(
        title='Movie 2',
        release_year=1999
    ))

    movie_3 = (Movie(
        title='Movie 3',
        release_year=2009
    ))

    actor_1 = (Actor(
        name='Actor 1',
        age=25,
        gender='male',
        movie_id=1
    ))

    actor_2 = (Actor(
        name='Actor 2',
        age=32,
        gender='male',
        movie_id=1
    ))

    actor_3 = (Actor(
        name='Actor 3',
        age=38,
        gender='female',
        movie_id=3
    ))

    actor_4 = (Actor(
        name='Actor 4',
        age=49,
        gender='female',
        movie_id=2
    ))

    movie_1.insert()
    movie_2.insert()
    movie_3.insert()
    actor_1.insert()
    actor_2.insert()
    actor_3.insert()


if __name__ == '__main__':
    db_test_records()
