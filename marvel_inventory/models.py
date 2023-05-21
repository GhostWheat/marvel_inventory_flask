from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
from datetime import datetime

# Adding Flask security for passwords
from werkzeug.security import generate_password_hash, check_password_hash


# import secrets module from python, generates a token for each user
import secrets

# import flask_login to chekc for authenticate user and store current user
from flask_login import UserMixin, LoginManager

#import flask marchmallow to help create aur Schemas
db = SQLAlchemy()
from flask_marshmallow import Marshmallow
login_manager = LoginManager()
ma = Marshmallow()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key = True)
    first_color = db.Column(db.String(150), nullable = True, default = '')
    last_color = db.Column(db.String(150), nullable = True, default = '')
    email = db.Column(db.String(150), nullable = False) #, unique = True
    password = db.Column(db.String(150), nullable = True, default= '')
    usercolor = db.Column(db.String(150), nullable = False) #, unique = True
    token = db.Column(db.String, default = '', unique = True)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    # come back later and add backref relationship
    hero = db.relationship('Hero', backref = 'owner', lazy = True)
    # this means the user can exist without associated hero existing/


    def __init__(self, email, usercolor, first_color = '', last_color = '', password = ''):
        self.id = self.set_id()
        self.first_color = first_color
        self.last_color = last_color
        self.password = self.set_password(password)
        self.email = email
        self.usercolor = usercolor
        self.token = self.set_token(24) # needs to set a length (24) of how long the token will be

    def set_token(self, length):
        return secrets.token_hex(length)

    def set_id(self):
        return str(uuid.uuid4())
    
    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash
    
    def __repr__(self):
        return f"User {self.email} has been added to the database!"
    

class Hero(db.Model):
    id = db.Column(db.String, primary_key = True)
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable=False)
    hero_name = db.Column(db.String(80))
    description = db.Column(db.String(1000))
    comics_appeared_in = db.Column(db.Numeric(precision=5, scale=0))
    super_power = db.Column(db.String(1000))
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)


    def __init__(self, user_token, hero_name, description, comics_appeared_in, super_power):
        self.id = self.set_id()
        self.user_token = user_token
        self.hero_name = hero_name
        self.description = description
        self.comics_appeared_in = comics_appeared_in
        self.super_power = super_power

    def set_id(self):
        return str(uuid.uuid4())

    def __repr__(self):
        return f"{self.id} {self.hero_name} has been added to the database!"
    
class HeroSchema(ma.Schema):
    class Meta:
      fields = ['id', 'hero_name', 'description','comics_appeared_in','super_power']

hero_schema = HeroSchema()
allheroes_schema = HeroSchema(many = True)

