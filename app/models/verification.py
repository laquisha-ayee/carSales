from .db import db, environment, SCHEMA, add_prefix_for_prod

class Verification(db.Model):
    __tablename__ = 'verifications'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('cars.id')), nullable=False)
    mechanic_name = db.Column(db.String(100), nullable=False)
    notes = db.Column(db.Text)
    verified = db.Column(db.Boolean, default=False)

    car = db.relationship('Car', back_populates='verification')

    def to_dict(self):
        return {
            'id': self.id,
            'car_id': self.car_id,
            'mechanic_name': self.mechanic_name,
            'notes': self.notes,
            'verified': self.verified
        }