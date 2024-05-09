from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI

import uvicorn


api = FastAPI()

connected_clients = {}
message_queue = []

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@api.get("/api/health")
async def root():
    return {"status": "OK"}


if __name__ == "__main__":
    uvicorn.run("main:api", port=3000, reload=True, workers=1)
