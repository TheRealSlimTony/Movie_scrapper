from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uvicorn
from requests_html import AsyncHTMLSession
from scraper import (
    obtener_peliculas_por_ubicacion,
    imprimir_informacion_peliculas,
)
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas las origines
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos
    allow_headers=["*"],  # Permite todos los headers
)


class Cartelera(BaseModel):
    location: Optional[str] = None


@app.post("/cartelera")
async def post_cartelera(cartelera: Cartelera):
    if cartelera.location:
        print(f"Ubicación proporcionada: {cartelera.location}")
        peliculas = await obtener_peliculas_por_ubicacion(cartelera.location)
        data_cartelera = imprimir_informacion_peliculas(peliculas, cartelera.location)
        return data_cartelera
    else:
        print("No se proporcionó ubicación")
        return {"message": "Cartelera creada sin ubicación específica"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
