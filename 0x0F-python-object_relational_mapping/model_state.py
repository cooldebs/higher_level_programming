#!/usr/bin/python3
"""
<<<<<<< HEAD
Contains State class and Base, an instance of declarative_base()
=======
Contains the class definition of a State and an
instance of declarative_base()
>>>>>>> 76a995ad7a3f61418ec390671e724d52e630da30
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
<<<<<<< HEAD
    """
    Class with id and name attributes of each state
    """
=======
    """ Class with id and name attributes of each state """
>>>>>>> 76a995ad7a3f61418ec390671e724d52e630da30
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
