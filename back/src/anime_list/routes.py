from fastapi import APIRouter, Depends

from .models import AnimeListCreate, AnimeListUpdate
from .service import AnimeListService
from shared.security import get_current_user
from users.models import User

router = APIRouter()


@router.get("/")
async def get_anime_lists():
    return await AnimeListService.get_all_anime_lists()


@router.get("/{list_id}")
async def get_anime_list(list_id: str):
    return await AnimeListService.get_anime_list_by_id(list_id)


@router.post("/")
async def post_anime_list(
    anime_list: AnimeListCreate, current_user: User = Depends(get_current_user)
):
    return await AnimeListService.create_anime_list(anime_list, current_user)


@router.put("/")
async def put_anime_list(
    anime_list: AnimeListUpdate, current_user: User = Depends(get_current_user)
):
    return await AnimeListService.update_anime_list(anime_list, current_user)


@router.delete("/{list_id}")
async def delete_anime_list(
    list_id: str, current_user: User = Depends(get_current_user)
):
    return await AnimeListService.delete_anime_list(list_id, current_user)
