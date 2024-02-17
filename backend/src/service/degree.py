from src.repository import degree as repository
from src.schemas import degree as schema
from src.utils import errors


def create(degree: schema.Create):
    """
    Create a new degree.
    """
    try:
        new_degree = repository.DegreeRepository.create(degree)
        return schema.Get(id=new_degree.id, university_id=new_degree.university_id, name=new_degree.name)
    except errors.DatabaseError:
        raise errors.InternalServerError("An error occurred while creating a degree.")
    except Exception:
        raise errors.InternalServerError("Internal server error.")


def get(university_id: int = None):
    """
    Retrieve all degrees by university.
    """
    try:
        degrees = repository.DegreeRepository.get(university_id)
        return [schema.Get(id=degree.id, university_id=degree.university_id, name=degree.name) for degree in degrees]
    except errors.DatabaseError:
        raise errors.InternalServerError("An error occurred while retrieving degrees.")
    except Exception:
        raise errors.InternalServerError("Internal server error.")


def delete(degree_id: int):
    """
    Delete a degree.
    """
    try:
        degree = repository.DegreeRepository.delete(degree_id)
        return schema.Get(id=degree.id, university_id=degree.university_id, name=degree.name)
    except errors.DatabaseError:
        raise errors.InternalServerError("An error occurred while deleting a degree.")
    except Exception:
        raise errors.InternalServerError("Internal server error.")


def update(degree_id: int, degree: schema.Create):
    """
    Update a degree.
    """
    try:
        update_degree = repository.DegreeRepository.update(degree, degree_id)
        return schema.Get(id=update_degree.id, university_id=update_degree.university_id, name=update_degree.name)
    except errors.DatabaseError:
        raise errors.InternalServerError("An error occurred while updating a degree.")
    except Exception:
        raise errors.InternalServerError("Internal server error.")
