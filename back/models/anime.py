from pydantic import BaseModel


class AnimeCreate(BaseModel):
    name: str
    amount_episodes: int
    author: str


class AnimeUpdate(BaseModel):
    anime_id: str
    name: str
    amount_episodes: int
    author: str
