from pydantic import BaseModel


class AnimeListCreate(BaseModel):
    list_name: str


class AnimeListUpdate(BaseModel):
    list_id: str
    name: str
