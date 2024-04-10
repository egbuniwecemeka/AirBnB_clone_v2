#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from models import storage
import shlex


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    @property
    def cities(self):
        """return cities with the current state_id"""
        objs = storage.all()
        lista = []
        results = []

        for key in objs:
            city = key.replace('.', ' ')
            city = shlex.split(" ")
            if (city[0] == 'City'):
                lista.append(objs[key])

        for elem in lista:
            if (elem.state_id == self.id):
                results.append(elem)
        return results
