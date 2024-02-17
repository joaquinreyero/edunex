from src.repository import university as repository
from src.schemas import university as schema
from src.utils import errors


def get_all_universities():
    """
    Get all universities.
    """
    try:
        universities = repository.UniversityRepository.get_all_university()
        return [schema.Get(id=uni.id, name=uni.name, abbreviation=uni.abbreviation) for uni in universities]
    except errors.DatabaseError as e:
        raise errors.DatabaseError("An error occurred while retrieving universities.")
    except Exception as e:
        raise errors.InternalServerError("An error occurred while retrieving universities.")


def create_university(university: schema.Create):
    """
    Create a new university.
    """
    try:
        university = repository.UniversityRepository.create_university(university)
        return schema.Get(id=university.id, name=university.name, abbreviation=university.abbreviation)
    except errors.DatabaseError as e:
        raise errors.DatabaseError("An error occurred while creating a university.")
    except Exception as e:
        raise errors.InternalServerError("An error occurred while creating a university.")


def get_university(university_id: int):
    """
    Get a university by id.
    """
    try:
        university = repository.UniversityRepository.get_university(university_id)
        return schema.Get(id=university.id, name=university.name, abbreviation=university.abbreviation)
    except errors.DatabaseError as e:
        raise errors.DatabaseError("An error occurred while retrieving a university.")
    except Exception as e:
        raise errors.InternalServerError("An error occurred while retrieving a university.")


def update_university(university: schema.Create, university_id: int):
    """
    Update a university by id.
    """
    try:
        university = repository.UniversityRepository.update_university(university, university_id)
        return schema.Get(id=university.id, name=university.name, abbreviation=university.abbreviation)
    except errors.DatabaseError as e:
        raise errors.DatabaseError("An error occurred while updating a university.")
    except Exception as e:
        raise errors.InternalServerError("An error occurred while updating a university.")


def delete_university(university_id: int):
    """
    Delete a university by id.
    """
    try:
        university = repository.UniversityRepository.delete_university(university_id)
        return schema.Get(id=university.id, name=university.name, abbreviation=university.abbreviation)
    except errors.DatabaseError as e:
        raise errors.DatabaseError("An error occurred while deleting a university.")
    except Exception as e:
        raise errors.InternalServerError("An error occurred while deleting a university.")
