import datetime

from pymongo import MongoClient
from pydantic import EmailStr

import bcrypt


class DatabaseService:
    def __init__(self, dsn: str):
        self.client = MongoClient(dsn)

        database_name = "sobeser"
        self.users_collection = self.client[database_name]["users"]

    async def register(self, email: EmailStr, password: str):
        hashed_password = bcrypt.hashpw(password=password.encode("utf-8"), salt=bcrypt.gensalt())
        self.users_collection.insert_one({
            "_id": self.users_collection.count_documents({}),
            "email": email,
            "hashed_password": hashed_password,
            "created_at": datetime.datetime.now(),
        })

        return self.users_collection.find_one({"email": email}, {"_id": False})

    async def get_user(self, email: EmailStr):
        return self.users_collection.find_one({"email": email}, {"_id": False})
