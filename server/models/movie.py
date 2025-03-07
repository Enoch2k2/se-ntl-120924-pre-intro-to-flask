from config import db
from sqlalchemy_serializer import SerializerMixin

class Movie(db.Model, SerializerMixin):
  __tablename__ = "movies"

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String)

  def __repr__(self):
    return f'<Movie id={self.id} title="{self.title}">'