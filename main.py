from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uvicorn
from requests_html import AsyncHTMLSession
from scraper import (
    obtener_peliculas_por_ubicacion,
    imprimir_informacion_peliculas,
)

app = FastAPI()


class Cartelera(BaseModel):
    Ubicacion: Optional[str] = None


@app.post("/cartelera")
async def post_cartelera(cartelera: Cartelera):
    if cartelera.Ubicacion:
        print(f"Ubicación proporcionada: {cartelera.Ubicacion}")
        peliculas = await obtener_peliculas_por_ubicacion(cartelera.Ubicacion)
        data_cartelera = imprimir_informacion_peliculas(peliculas, cartelera.Ubicacion)
        return {
            "La cartelera de {} es la siguiente: {}".format(
                cartelera.Ubicacion, data_cartelera
            )
        }
    else:
        print("No se proporcionó ubicación")
        return {"message": "Cartelera creada sin ubicación específica"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
