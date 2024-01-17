from requests_html import AsyncHTMLSession
import asyncio
import re


async def obtener_peliculas_por_ubicacion(ubicacion):
    session = AsyncHTMLSession()
    try:
        url = f"https://cinepolis.co.cr/cartelera/{ubicacion}/"
        response = await session.get(url)
        # Usa create_task para ejecutar render de forma asíncrona
        await asyncio.create_task(response.html.arender())
        return response.html.find("article")
    finally:
        await session.close()


def extraer_informacion(pelicula):
    # Intenta extraer el título
    match_titulo = re.match(r".*?(?=(?:TP)?M?\d+|\d+ min)", pelicula)
    titulo = match_titulo.group() if match_titulo else "Título no encontrado"

    # Intenta extraer la duración en minutos
    match_duracion = re.search(r"(\d{1,3}) min", pelicula)
    duracion = (
        f"{match_duracion.group(1)} minutos"
        if match_duracion
        else "Duración no encontrada"
    )

    # Extrae horarios SUB y DOB
    sub_horarios = re.findall(r"SUB((?:\d{2}:\d{2})+)", pelicula)
    dob_horarios = re.findall(r"DOB((?:\d{2}:\d{2})+)", pelicula)

    sub_horarios_separados = re.findall(r"\d{2}:\d{2}", "".join(sub_horarios))
    dob_horarios_separados = re.findall(r"\d{2}:\d{2}", "".join(dob_horarios))

    return titulo, duracion, sub_horarios_separados, dob_horarios_separados


def imprimir_informacion_peliculas(peliculas, ubicacion):
    cartelera_info = []
    for pelicula in peliculas:
        titulo, duracion, horarios_sub, horarios_dob = extraer_informacion(
            pelicula.full_text
        )
        if titulo != "Título no encontrado":
            pelicula_info = {
                "título": titulo,
                "duración": duracion,
                "horarios_sub": horarios_sub,
                "horarios_dob": horarios_dob,
            }
            cartelera_info.append(pelicula_info)

    return cartelera_info
