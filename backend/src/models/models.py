from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class IdTimeStampIsActiveMixin:
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)


class University(IdTimeStampIsActiveMixin, Base):
    __tablename__ = 'university'

    name = Column(String, nullable=False, unique=True)
    abbreviation = Column(String, nullable=False, unique=True)


class Degree(IdTimeStampIsActiveMixin, Base):
    __tablename__ = 'degree'

    university_id = Column(Integer, ForeignKey('university.id'), nullable=False)

    name = Column(String, nullable=False)


class Subject(IdTimeStampIsActiveMixin, Base):
    __tablename__ = 'subject'

    degree_id = Column(Integer, ForeignKey('degree.id'), nullable=False)

    name = Column(String, nullable=False)
    year = Column(Integer, nullable=False)


class Tutor(IdTimeStampIsActiveMixin, Base):
    __tablename__ = 'tutor'

    degree_id = Column(Integer, ForeignKey('degree.id'), nullable=False)

    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    cel = Column(String, nullable=False, unique=True)
    description = Column(Text, nullable=True)
    photo = Column(String, nullable=True)


class Tutoring(IdTimeStampIsActiveMixin, Base):
    __tablename__ = 'tutoring'

    subject_id = Column(Integer, ForeignKey('subject.id'), nullable=False)
    tutor_id = Column(Integer, ForeignKey('tutor.id'), nullable=False)

    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Float, nullable=True)
    payment = Column(String, nullable=True)
    student_type = Column(String, nullable=True)
    modality = Column(String, nullable=True)
    tutoring_type = Column(String, nullable=True)
    includes = Column(Text, nullable=True)
