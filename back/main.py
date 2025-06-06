from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.shared.database import Database

from src.test_vercel.routes import router as test_vercel_router
from src.users.routes import router as user_router
from src.auth.routes import router as auth_router
from src.genres.routes import router as genre_router
from src.anime_list.routes import router as list_router
from src.anime_genre.routes import router as anime_genre_router
from src.animes.routes import router as anime_router
from src.anime_lists_animes.routes import router as anime_lists_animes_router

from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 🚀 Inicializar el pool al iniciar la app
    await Database.init_pool()
    print("Database pool iniciado")

    yield  # 🟢 La app corre aquí

    # 🛑 Cerrar el pool al apagar la app
    await Database.close_pool()
    print("Database pool cerrado")


app = FastAPI(title="Anime API", lifespan=lifespan)

origins = ["http://localhost:4200"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(test_vercel_router, prefix="/api/testvercel")

app.include_router(auth_router, prefix="/api/auth", tags=["Auth"])
app.include_router(user_router, prefix="/api/users", tags=["Users"])
app.include_router(genre_router, prefix="/api/genres", tags=["Genre"])
app.include_router(list_router, prefix="/api/lists", tags=["Anime List"])
app.include_router(anime_genre_router, prefix="/api/anime_genre", tags=["Anime Genre"])
app.include_router(anime_router, prefix="/api/anime", tags=["Anime"])
app.include_router(
    anime_lists_animes_router,
    prefix="/api/anime_lists_animes",
    tags=["Anime Lists Animes"],
)

# Agrega esto para que Vercel pueda ejecutarlo
import os

if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
