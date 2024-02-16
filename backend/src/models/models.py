from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Boolean, Enum

Base = declarative_base()

class Test(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True, index=True)