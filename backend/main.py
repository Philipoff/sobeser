from starlette.middleware.cors import CORSMiddleware
from services.service import APIService
from database.database import DatabaseService

import uvicorn

api = APIService(DatabaseService("mongodb+srv://philip:zJc1qYPe1LBhyQiz@sobeser.rihv0sq.mongodb.net/?retryWrites=true&w=majority&appName=sobeser"))

api.app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@api.app.get("/api/health")
async def root():
    return {"status": "OK"}


if __name__ == "__main__":
    uvicorn.run("main:api.app", port=3000, reload=True, workers=1)