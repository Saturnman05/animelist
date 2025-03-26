from fastapi import APIRouter, Depends

from .models import AnimeListsAnimes
from .service import AnimeListsAnimesService
from shared.security import get_current_user
from users.models import User

router = APIRouter()


@router.get("/")
async def get_anime_lists_animes(
    list_id: str | None = None,
    anime_id: str | None = None,
    _: User = Depends(get_current_user),
):
    return await AnimeListsAnimesService.get_all_anime_list_animes(list_id, anime_id)


@router.post("/")
async def post_anime_lists_animes(
    anime_lists_animes: AnimeListsAnimes, _: User = Depends(get_current_user)
):
    return await AnimeListsAnimesService.create_anime_list_animes(anime_lists_animes)


@router.delete("/")
async def delete_anime_lists_animes(
    anime_lists_animes: AnimeListsAnimes, _: User = Depends(get_current_user)
):
    return await AnimeListsAnimesService.delete_anime_list_anime(anime_lists_animes)
