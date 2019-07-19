from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


from app import db


# import sqlalchemy
# models.User.query.from_statement(sqlalchemy.text('SELECT * FROM User')).all()
# models.User.query.get(1)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    # The field above is not an actual database field, but a high-level view of the relationship between users and posts
    # For a one-to-many relationship, a db.relationship field is normally defined on the "one" side, and is used as
    # a convenient way to get access to the "many"
    # The first argument to db.relationship is the model class that represents the "many" side of the relationship
    # The backref argument defines the name of a field that will be added to the objects of the "many" class that
    # points back at the "one" object.
    # The lazy argument defines how the database query for the relationship will be issued,
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username) 


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # It is an unfortunate inconsistency that in some instances such as in a db.relationship() call,
    # the model is referenced by the model class, which typically starts with an uppercase character,
    # while in other cases such as this db.ForeignKey() declaration, a model is given by its database table name,
    # for which SQLAlchemy automatically uses lowercase characters and, for multi-word model names, snake case

    def __repr__(self):
        return '<Post {}>'.format(self.body)
