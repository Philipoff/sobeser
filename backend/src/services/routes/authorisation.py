from fastapi import APIRouter, status, Request, HTTPException

from ...services.schemas.auth import RestCredentials
from ...services.jwt_processing import Auth
from ...database.database import DatabaseService

auth_router = APIRouter(
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)


@auth_router.post("/login")
async def login(request: Request, data: RestCredentials):
    database: DatabaseService = request.app.state.database

    auth = Auth()
    user = await database.get_user(email=data.email)

    if user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Неверный e-mail!')
    if not auth.verify_password(data.password, user["hashed_password"]):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Неверный пароль')

    access_token = auth.create_token(data.email)
    refresh_token = auth.create_refresh_token(data.email)

    return {"access_token": access_token, "refresh_token": refresh_token}


@auth_router.post(
    path="/register",
    status_code=status.HTTP_200_OK,
    responses={400: {}, 401: {}, 403: {}},
)
async def register(request: Request, data: RestCredentials):
    database: DatabaseService = request.app.state.database
    auth = Auth()
    user = await database.get_user(email=data.email)

    if user is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ввёденный e-mail уже используется.",
        )

    await database.register(
        email=data.email,
        password=data.password,
    )

    access_token = auth.create_token(data.email)
    refresh_token = auth.create_refresh_token(data.email)

    return {"access_token": access_token, "refresh_token": refresh_token}
