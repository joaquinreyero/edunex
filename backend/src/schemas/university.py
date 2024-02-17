from pydantic import BaseModel


class Get(BaseModel):
    id: int
    name: str
    abbreviation: str


class Create(BaseModel):
    name: str
    abbreviation: str

    class Config:
        orm_mode = True
