from fastapi import Depends, status, APIRouter

from src.service import tutor as service
from src.schemas import tutor as schema

router = APIRouter(
    prefix="/api",
    tags=["Tutor"],
)

@router.post("/login", status_code=status.HTTP_200_OK, response_model=str)
async def login( credentials: schema.Login):
    """
    Login a User
    """
    return service.Login(credentials)

@router.post("/subject", status_code=status.HTTP_201_CREATED, response_model=schema.Get)
async def create(subject: schema.Create):
    """
    Create a new subject.
    """
    return service.create(subject)


@router.get("/subjects", status_code=status.HTTP_200_OK, response_model=list[schema.Get])
async def get(subject_id: int = None):
    """
    Retrieve all subjects by degree.
    """
    return service.get(subject_id)


@router.delete("/subject/{subject_id}", status_code=status.HTTP_200_OK, response_model=schema.Get)
async def delete(subject_id: int):
    """
    Delete a subject.
    """
    return service.delete(subject_id)


@router.put("/subject/{subject_id}", status_code=status.HTTP_200_OK, response_model=schema.Get)
async def update(subject_id: int, subject: schema.Create):
    """
    Update a subject.
    """
    return service.update(subject_id, subject)

