import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)


# class Post(Base):
#     __tablename__ = 'post'
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey('user.id'))
#     comment_text = Column(String(250), nullable=False)


class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    # post_id = Column(Integer, ForeignKey('post.id'))
    people_id = Column(Integer, ForeignKey('people.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))


class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    created = Column(String(250), nullable=False)
    edited = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    homeworld = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)


class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    diameter = Column(Integer, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    gravity = Column(String(250), nullable=False)
    population = Column(Integer, nullable=False)
    climate = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    surface_water = Column(Integer, nullable=False)
    created = Column(String(250), nullable=False)
    edited = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)




    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
