from pydantic import BaseModel


class AnimeListsAnimes(BaseModel):
    list_id: str
    anime_id: str
