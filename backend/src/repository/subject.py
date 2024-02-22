from sqlalchemy.exc import SQLAlchemyError

from src.config import configure_database
from src.models import models
from src.schemas import subject as schema
from src.utils import errors


class SubjectRepository:

    @staticmethod
    def create(subject: schema.Create):
        db = configure_database()
        try:
            new_subject = models.Subject(
                name=subject.name,
                year=subject.year,
                degree_id=subject.degree_id
            )
            db.add(new_subject)
            db.commit()
            db.refresh(new_subject)
            return new_subject
        except SQLAlchemyError as e:
            db.rollback()
            raise errors.DatabaseError("An error occurred while creating a subject.")

    @staticmethod
    def get(degree_id: int = None):
        db = configure_database()
        try:
            if degree_id:
                subjects = db.query(models.Subject).filter(models.Subject.degree_id == degree_id).all()
            else:
                subjects = db.query(models.Subject).all()
            return subjects
        except SQLAlchemyError as e:
            db.rollback()
            raise errors.DatabaseError("An error occurred while retrieving subjects.")

    @staticmethod
    def delete(subject_id: int):
        db = configure_database()
        try:
            subject = db.query(models.Subject).filter(models.Subject.id == subject_id).first()
            if subject:
                db.delete(subject)
                db.commit()
                return subject
            else:
                raise errors.DatabaseError("Subject not found with id: {}".format(subject_id))
        except SQLAlchemyError as e:
            db.rollback()
            raise errors.DatabaseError("An error occurred while deleting the subject: {}".format(str(e)))

    @staticmethod
    def update(subject: schema.Create, subject_id: int):
        db = configure_database()
        try:
            db.query(models.Subject).filter(models.Subject.id == subject_id).update({
                'name': subject.name,
                'year': subject.year,
                'university_id': subject.university_id
            })
            db.commit()
            return db.query(models.Subject).filter(models.Subject.id == subject_id).first()
        except SQLAlchemyError as e:
            db.rollback()
            raise errors.DatabaseError("An error occurred while updating the subject.")
