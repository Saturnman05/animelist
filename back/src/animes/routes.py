from fastapi import APIRouter, Depends

from .models import AnimeCreate, AnimeUpdate
from .service import AnimeService
from src.shared.security import get_current_user

router = APIRouter()


@router.get("/")
async def get_animes(
    name: str | None = None,
    amount_episodes: int | None = None,
    author: str | None = None,
):
    return await AnimeService.get_all_animes(name, amount_episodes, author)


@router.get("/{anime_id}")
async def get_anime(anime_id: str):
    return await AnimeService.get_anime_by_id(anime_id)


@router.post("/")
async def post_anime(anime: AnimeCreate, _: str = Depends(get_current_user)):
    return await AnimeService.create_anime(anime)


@router.put("/")
async def put_anime(anime: AnimeUpdate, _: str = Depends(get_current_user)):
    return await AnimeService.update_anime(anime)


@router.delete("/{anime_id}")
async def delete_anime(anime_id: str, _: str = Depends(get_current_user)):
    return await AnimeService.delete_anime(anime_id)
