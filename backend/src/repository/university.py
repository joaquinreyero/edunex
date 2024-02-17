from sqlalchemy.exc import SQLAlchemyError

from src.config import configure_database
from src.models import models
from src.schemas import university as schema
from src.utils import errors


class UniversityRepository:
    @staticmethod
    def get_all_university():
        db = configure_database()
        try:
            university = db.query(models.University).all()
            return university
        except SQLAlchemyError as e:
            db.rollback()
            raise errors.DatabaseError("An error occurred while retrieving universities.")

    @staticmethod
    def create_university(university: schema.Create):
        db = configure_database()
        try:
            new_university = models.University(
                name=university.name,
                abbreviation=university.abbreviation
            )
            db.add(new_university)
            db.commit()
            db.refresh(new_university)
            return new_university
        except SQLAlchemyError as e:
            db.rollback()
            raise errors.DatabaseError("An error occurred while creating universities.")

    @staticmethod
    def get_university(university_id: int):
        db = configure_database()
        try:
            university = db.query(models.University).filter(models.University.id == university_id).first()
            return university
        except SQLAlchemyError as e:
            db.rollback()
            raise errors.DatabaseError("An error occurred while retrieving university.")

    @staticmethod
    def update_university(university: schema.Create, university_id: int):
        db = configure_database()
        try:
            db.query(models.University).filter(models.University.id == university_id).update({
                'name': university.name,
                'abbreviation': university.abbreviation
            })
            db.commit()
            return db.query(models.University).filter(models.University.id == university_id).first()
        except SQLAlchemyError as e:
            db.rollback()
            raise errors.DatabaseError("An error occurred while updating universities.")

    @staticmethod
    def delete_university(university_id: int):
        db = configure_database()
        try:
            university = db.query(models.University).filter(models.University.id == university_id).first()
            db.delete(university)
            db.commit()
            return university
        except SQLAlchemyError as e:
            db.rollback()
            raise errors.DatabaseError("An error occurred while deleting universities.")
