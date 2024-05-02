from fastapi import FastAPI
from fastapi.security import HTTPBearer
from pydantic import BaseModel
from typing import Optional
import uvicorn
from requests_html import AsyncHTMLSession
from scraper import (
    obtener_peliculas_por_ubicacion,
    imprimir_informacion_peliculas,
    obtener_imagenes,
)
from scraper_by_api_request import get_data_from_movies, get_data_from_cinema_id
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
Security = HTTPBearer()

origins = [
    "http://localhost:3000", 
    "http://localhost:8000",
    "http://127.0.0.1:8000", 
    "https://cinepolisscrapper.azurewebsites.net",
    "https://cinepolisscrapperui.azurewebsites.net",
    "cinepolisscrapperui.azurewebsites.net",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,  # Permite todas las origines
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos
    allow_headers=["*"],  # Permite todos los headers
)

class Cartelera(BaseModel):
    # location: Optional[str] = None
    cinema_id: Optional[int] = None

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/cartelera")
async def post_cartelera(cartelera: Cartelera):
    if cartelera.cinema_id:
        data = get_data_from_cinema_id(cartelera.cinema_id)
        movies = data['schedules']['movies']
        movie_schedules = data['schedules']['schedules']
        data_cartelera = get_data_from_movies(movies, movie_schedules)
        return data_cartelera
    else:
        print("No se proporcionó ubicación")
        return {"message": "Cartelera creada sin ubicación específica"}

@app.post("/all_movies")
async def post_all_movies():
    peliculas = await obtener_peliculas_por_ubicacion(ubicacion="moravia-costa-rica")
    all_movies = obtener_imagenes(peliculas, ubicacion="moravia-costa-rica")
    return all_movies

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)
