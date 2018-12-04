from sqlalchemy import Column, Integer, String, Float
from app import db

class Call(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    call_type = db.Column(db.Integer)
    street = db.Column(db.String(250))
    number = db.Column(db.Integer)
    neighborhood = db.Column(db.String(250))
    city = db.Column(db.String(250))
    state = db.Column(db.String(250))
    complement = db.Column(db.String(250))
    observation = db.Column(db.String(250))
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)

    def __repr__(self):
        return "ID = '%s', Street = '%s', Number = '%s'" % (self.id, self.street, self.number)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'call_type': self.call_type,
            'street': self.street,
            'number': self.number,
            'neighborhood': self.neighborhood,
            'city': self.city,
            'state': self.state,
            'lat': self.lat,
            'lng': self.lng
        }

    
