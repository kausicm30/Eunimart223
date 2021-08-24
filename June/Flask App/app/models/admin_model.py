from app import db

class Owner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    theatres= db.relationship('Movie',backref='owner')

    def __init__(self,email,password):
        self.email = email
        self.password = password