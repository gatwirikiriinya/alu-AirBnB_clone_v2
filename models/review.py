#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Review(BaseModel):
    """ Review classto store review information """
    place_id = ""
    user_id = ""
    text = ""
    
    __tablename__ = "reviews"

    place_id = Column(String(60), nullable=False)
    user_id = Column(String(60), nullable=False)
    text = Column(String(1024), nullable=False)
    users = relationship("User", backref="user", cascade="delete")
