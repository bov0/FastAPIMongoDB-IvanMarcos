from fastapi import FastAPI
from routes.animal import animal

app = FastAPI()

app.include_router(animal)

