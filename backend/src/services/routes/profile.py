from fastapi import APIRouter, status, Request, HTTPException
from ...services.schemas.profile import RestToken
from ...database.database import DatabaseService
from ...services.jwt_processing import Auth

profile_router = APIRouter(
    tags=["profile"],
    responses={404: {"description": "Not found"}},
)


@profile_router.post("/info")
async def info(request: Request, token: RestToken):
    database: DatabaseService = request.app.state.database

    auth = Auth()
    data = auth.decode_token(token.token)
    user = await database.get_user(email=data["email"])
    user["created_at"] = user["created_at"].strftime("%d/%m/%y")
    print(user)

    return user
