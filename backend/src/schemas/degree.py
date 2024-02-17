from pydantic import BaseModel


class Get(BaseModel):
    id: int
    name: str
    university_id: int


class Create(BaseModel):
    name: str
    university_id: int
