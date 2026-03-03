#!/usr/bin/python3
"""
Contains the class definition of a State and instance Base
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Instance de Base pour l'ORM
Base = declarative_base()


class State(Base):
    """
    Class State that links to MySQL table 'states'
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
