import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()

class Category(Base):

    __tablename__ = 'category'

    name = Column(String(12), nullable = False)
    id = Column(Integer, primary_key = True)

class Resource(Base):

    __tablename__ = 'resource'

    id = Column(Integer, primary_key = True)
    name = Column(String(12), nullable = False)
    description = Column(String (250))
    category_id = Column(ForeignKey('category.id'))
    cateogry = relationship(Category)

engine = create_engine('sqlite:///resources.db')
Base.metadata.create_all(engine)
