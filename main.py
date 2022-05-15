from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
import multiprocessing
from docs import my_schema
from api import routes

load_dotenv()

api = FastAPI()

api.include_router(routes.router)


origins = []
api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def number_of_workers():
    return (multiprocessing.cpu_count() * 2) + 1


@api.get("/test")
async def root():
    return {"msg": "API is Online"}


my_schema(api)

if __name__ == "__main__":
    if os.environ.get('APP_ENV') == "development":
        uvicorn.run("main:api", host="0.0.0.0", port=7001,
                    workers=4, reload=True)

    else:
        uvicorn.run("main:api", host="0.0.0.0", port=7001,
                    workers=number_of_workers())
