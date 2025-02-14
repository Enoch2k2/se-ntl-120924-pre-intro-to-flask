from config import app, db
from models.models import *

if __name__ == "__main__":
  with app.app_context():
    Movie.query.delete()

    movie_1 = Movie(title="Back to the Future")
    movie_2 = Movie(title="Teenage Mutant Ninja Turtles")

    db.session.add(movie_1)
    db.session.add(movie_2)
    db.session.commit()
    # remove pass and write your seed data

    print("Finished Seeding")
