from fastapi import Depends, status, APIRouter

from src.service import degree as service
from src.schemas import degree as schema

router = APIRouter(
    prefix="/api",
    tags=["Degree"],
)


@router.post("/degree", status_code=status.HTTP_201_CREATED, response_model=schema.Get)
async def create(degree: schema.Create):
    """
    Create a new degree.
    """
    return service.create(degree)


@router.get("/degrees", status_code=status.HTTP_200_OK, response_model=list[schema.Get])
async def get(university_id: int = None):
    """
    Retrieve all degrees by university.
    """
    return service.get(university_id)


@router.delete("/degree/{degree_id}", status_code=status.HTTP_200_OK, response_model=schema.Get)
async def delete(degree_id: int):
    """
    Delete a degree.
    """
    return service.delete(degree_id)


@router.put("/degree/{degree_id}", status_code=status.HTTP_200_OK, response_model=schema.Get)
async def update(degree_id: int, degree: schema.Create):
    """
    Update a degree.
    """
    return service.update(degree_id, degree)
