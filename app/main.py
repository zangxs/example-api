from fastapi import FastAPI
from app.controllers.weatherController import router
from app.entities.weatherEntity import WeatherEntity
from app.config.database import Base, engine

Base.metadata.create_all(bind=engine)  # crea las tablas al arrancar



app = FastAPI()
app.include_router(router)

@app.get("/")
def read_root():
    return {"Hello": "Mundo"}