from fastapi import FastAPI

from fastapi_sandwiches.routers import home

app = FastAPI()

app.include_router(home.router)
