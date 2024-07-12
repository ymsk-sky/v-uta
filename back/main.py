from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from controllers.controller import router
from repositories.database import engine
from repositories.models import Base


Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
