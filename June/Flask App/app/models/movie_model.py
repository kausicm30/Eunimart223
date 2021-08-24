from app import db
from app.models.admin_model import Owner

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_id =db.Column(db.ForeignKey('owner.id'))
    movie_name = db.Column(db.String(100))
    movie_time = db.Column(db.String(100))
    theatre_name = db.Column(db.String(100))

    def __init__(self,owner_id,movie_name, movie_time, theatre_name):
        self.owner_id = owner_id
        self.movie_name = movie_name
        self.movie_time = movie_time
        self.theatre_name = theatre_name