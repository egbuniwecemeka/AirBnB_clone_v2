#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
import models
from os import getenv


class State(BaseModel, Base):
    """ State for MySQL DB

        Inherits from MySQLQlchemy Base to MySQL tables

        Attribute:
        __tablename__(str): Name of MySQL table storing states
        name (str): Name of state
        city (sqlalchemy relationship): State-City order.
    """
    __tablename__ = "states"

    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="states", cascade="all, delete")
    else:
        name = ""
    
    @property
    def cities(self):
        """Gets list of city instances with the current state_id
            Getter attribute for Filestorage relationship btw
            states and cities
        """
        cities = []
        for city in models.storage.all(City).values():
            if city.state_id == self.id:
                cities.append(city)
        return cities
