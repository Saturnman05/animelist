from pydantic import BaseModel


class GenreCreate(BaseModel):
    name: str


class GenreUpdate(BaseModel):
    genre_id: str
    name: str
