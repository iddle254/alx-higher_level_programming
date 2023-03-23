#!/usr/bin/python3
"""
contains the class definition of a State and an instance
Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    """ State class model that maps to a states table """
    __tablename__ = 'states'

    id = Column(Integer, Sequence('state_id_seq'),
                primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    cities = relationship("City", back_populates="state")
