from src.repository import tutor as repository
from src.schemas import tutor as schema
from src.utils import errors


def create(credentials: schema.Login):
    """
    Login a User.
    """
    try:
        user_logged = repository.SubjectRepository.create(subject)
        return schema.Get(id=new_subject.id, degree_id=new_subject.degree_id, name=new_subject.name,
                          year=new_subject.year)
    except errors.DatabaseError:
        raise errors.InternalServerError("An error occurred while creating a subject.")
    except Exception:
        raise errors.InternalServerError("Internal server error.")


