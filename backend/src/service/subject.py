from src.repository import subject as repository
from src.schemas import subject as schema
from src.utils import errors


def create(subject: schema.Create):
    """
    Create a new subject.
    """
    try:
        new_subject = repository.SubjectRepository.create(subject)
        return schema.Get(id=new_subject.id, degree_id=new_subject.degree_id, name=new_subject.name,
                          year=new_subject.year)
    except errors.DatabaseError:
        raise errors.InternalServerError("An error occurred while creating a subject.")
    except Exception:
        raise errors.InternalServerError("Internal server error.")


def get(subject_id: int = None):
    """
    Retrieve all subjects by degree.
    """
    try:
        subjects = repository.SubjectRepository.get(subject_id)
        return [schema.Get(id=subject.id, degree_id=subject.degree_id, name=subject.name, year=subject.year)
                for subject in subjects]
    except errors.DatabaseError:
        raise errors.InternalServerError("An error occurred while retrieving subjects.")
    except Exception:
        raise errors.InternalServerError("Internal server error.")


def delete(subject_id: int):
    """
    Delete a subject.
    """
    try:
        subject = repository.SubjectRepository.delete(subject_id)
        return schema.Get(id=subject.id, university_id=subject.university_id, name=subject.name, year=subject.year)
    except errors.DatabaseError:
        raise errors.InternalServerError("An error occurred while deleting a subject.")
    except Exception:
        raise errors.InternalServerError("Internal server error.")


def update(subject_id: int, subject: schema.Create):
    """
    Update a subject.
    """
    try:
        update_subject = repository.SubjectRepository.update(subject, subject_id)
        return schema.Get(id=update_subject.id, university_id=update_subject.university_id, name=update_subject.name, year=update_subject.year)
    except errors.DatabaseError:
        raise errors.InternalServerError("An error occurred while updating a subject.")
    except Exception:
        raise errors.InternalServerError("Internal server error.")
