from config import api, db
from flask import request
from flask_restful import Resource
from models.models import Movie

class MoviesResource(Resource): # /movies GET, POST
  def get(self):
    movies = Movie.query.all()
    movie_dicts = [movie.to_dict() for movie in movies]
    return movie_dicts, 200
  
  def post(self):
    # needs to retrieve data sent
    data = request.get_json()
    title = data.get("title")
    # create and save a movie from the data
    movie = Movie(title=title)
    db.session.add(movie)
    db.session.commit()
    # return new movie as json
    return movie.to_dict(), 201

class MovieResource(Resource): # /movies/1 GET, PATCH, DELETE
  def get(self, id):
    # find the one movie by id
    movie = Movie.query.get(id)
    # return that movie as json
    return movie.to_dict(), 200
  
  def patch(self, id):
    data = request.get_json()
    title = data.get("title")
    movie = Movie.query.get(id)
    movie.title = title
    db.session.add(movie)
    db.session.commit()

    return movie.to_dict(), 200
  
  def delete(self, id):
    movie = Movie.query.get(id)
    db.session.delete(movie)
    db.session.commit()

    return {}, 204


api.add_resource(MoviesResource, "/api/movies")
api.add_resource(MovieResource, "/api/movies/<int:id>")