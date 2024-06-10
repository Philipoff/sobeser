from src.services.service import APIService
from src.database.database import DatabaseService

import uvicorn

api = APIService(DatabaseService("mongodb+srv://philip:zJc1qYPe1LBhyQiz@sobeser.rihv0sq.mongodb.net/?retryWrites=true&w=majority&appName=sobeser"))


@api.app.get("/api/health")
async def root():
    return {"status": "OK"}


if __name__ == "__main__":
    uvicorn.run("main:api.app", port=3000, reload=True, workers=1)
