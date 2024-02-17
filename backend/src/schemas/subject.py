from pydantic import BaseModel


class Get(BaseModel):
    id: int
    name: str
    year: int
    degree_id: int


class Create(BaseModel):
    name: str
    year: int
    degree_id: int
