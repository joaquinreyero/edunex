from sqlalchemy.exc import SQLAlchemyError

from src.config import configure_database
from src.models import models
from src.schemas import degree as schema
from src.utils import errors


class DegreeRepository:

    @staticmethod
    def create(degree: schema.Create):
        db = configure_database()
        try:
            new_degree = models.Degree(
                name=degree.name,
                university_id=degree.university_id
            )
            db.add(new_degree)
            db.commit()
            db.refresh(new_degree)
            return new_degree
        except SQLAlchemyError as e:
            db.rollback()
            raise errors.DatabaseError("An error occurred while creating a degree.")

    @staticmethod
    def get(university_id: int = None):
        db = configure_database()
        try:
            if university_id:
                degrees = db.query(models.Degree).filter(models.Degree.university_id == university_id).all()
            else:
                degrees = db.query(models.Degree).all()
            return degrees
        except SQLAlchemyError as e:
            db.rollback()
            raise errors.DatabaseError("An error occurred while retrieving degrees.")

    @staticmethod
    def delete(degree_id: int):
        db = configure_database()
        try:
            degree = db.query(models.Degree).filter(models.Degree.id == degree_id).first()
            db.delete(degree)
            db.commit()
            return degree
        except SQLAlchemyError as e:
            db.rollback()
            raise errors.DatabaseError("An error occurred while retrieving degrees.")

    @staticmethod
    def update(degree: schema.Create, degree_id: int):
        db = configure_database()
        try:
            db.query(models.Degree).filter(models.Degree.id == degree_id).update({
                'name': degree.name,
                'university_id': degree.university_id
            })
            db.commit()
            return db.query(models.Degree).filter(models.Degree.id == degree_id).first()
        except SQLAlchemyError as e:
            db.rollback()
            raise errors.DatabaseError("An error occurred while retrieving degrees.")
