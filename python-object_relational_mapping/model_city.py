#!/usr/bin/python3
"""
Contains the class definition of City.
"""


import sys
from sqlalchemy import (
    Integer,
    String,
    Column,
    ForeignKey
)
from model_state import State
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    """The City class declaration"""
    __tablename__ = "cities"
    id = Column(
        Integer,
        autoincrement=True,
        unique=True,
        nullable=False,
        primary_key=True
    )
    name = Column(
        String(128),
        nullable=False
    )
    state_id = Column(
        Integer,
        ForeignKey(State.id),
        nullable=False
    )
