from aiomysql import DictCursor
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException, Security
from fastapi.security import OAuth2PasswordBearer
import jwt

from database import Database
from utils.consts import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from models.user import User


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (
        expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/login")


async def get_current_user(token: str = Security(oauth2_scheme)):
    """Verifica el token JWT y obtiene el usuario."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Token inválido")

        async with await Database.get_connection() as con:
            async with con.cursor(DictCursor) as cursor:
                await cursor.execute(
                    "CALL sp_users(%s, NULL, NULL, NULL, 2)", (user_id,)
                )
                result = await cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Usuario no encontrado")

        user = User(
            user_id=result["user_id"],
            username=result["username"],
            email=result["email"],
            password=result["password"],
        )
        return user
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token inválido")
