from pydantic import BaseModel


class RestToken(BaseModel):
    token: str
