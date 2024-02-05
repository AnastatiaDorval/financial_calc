from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique = True, nullable = False)
    gross_income = db.Column(db.Float, nullable = True)
    income = db.Column(db.Float, nullable = True)
    # contributions = db.relationship('Contribution', backref='user')

    def __repr__(self):
        return f'<User {self.username}>'
    
class Contribution(db.Model):
    __tablename__ = 'contribution'
    id = db.Column(db.Integer, primary_key=True)
    before_tax = db.Column(db.Float, nullable=True)
    after_tax = db.Column(db.Float, nullable=True)
    roth_401k = db.Column(db.Float, nullable=True)
    roth_ira = db.Column(db.Float, nullable=True)
    traditional_ira = db.Column(db.Float, nullable=True)
    brokerage = db.Column(db.Float, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    __table_args__ = (
        CheckConstraint('before_tax < 1', name = 'Check before_tax contribution is less than 100%'),
        CheckConstraint('after_tax < 1', name = 'Check after_tax contribution is less than 100%'),
        CheckConstraint('roth_401k < 1', name = 'Check roth_401K contribution is less than 100%')
    )

    def __repr__(self):
        return f'<Contributions {self.roth_401k}>'