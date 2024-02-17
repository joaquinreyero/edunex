from fastapi import Depends, status, APIRouter

from src.service import university as service
from src.schemas import university as schema

router = APIRouter(
    prefix="/api",
    tags=["University"],
)


@router.get("/universities", status_code=status.HTTP_200_OK, response_model=list[schema.Get])
async def get_all_universities():
    """
    Get all universities.
    """
    return service.get_all_universities()


@router.post("/university", status_code=status.HTTP_201_CREATED, response_model=schema.Get)
async def create_university(university: schema.Create):
    """
    Create a new university.
    """
    return service.create_university(university)


@router.get("/university/{university_id}", status_code=status.HTTP_200_OK, response_model=schema.Get)
async def get_university(university_id: int):
    """
    Get a university by id.
    """
    return service.get_university(university_id)


@router.put("/university/{university_id}", status_code=status.HTTP_200_OK, response_model=schema.Get)
async def update_university(university: schema.Create, university_id: int):
    """
    Update a university by id.
    """
    return service.update_university(university, university_id)


@router.delete("/university/{university_id}", status_code=status.HTTP_200_OK, response_model=schema.Get)
async def delete_university(university_id: int):
    """
    Delete a university by id.
    """
    return service.delete_university(university_id)
