from pydantic import BaseModel, EmailStr


class RestCredentials(BaseModel):
    email: EmailStr
    password: str
