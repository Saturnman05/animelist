from pydantic import BaseModel


class AnimeGenre(BaseModel):
    anime_id: str
    genre_id: str
