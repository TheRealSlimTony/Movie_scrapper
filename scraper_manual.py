import re
from requests_html import HTMLSession


def obtener_peliculas_por_ubicacion(ubicacion):
    session = HTMLSession()
    url = f"https://cinepolis.co.cr/cartelera/{ubicacion}/"
    r = session.get(url)
    r.html.render()
    return r.html.find("article")


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
    print(f"\nCartelera para: {ubicacion}")
    for pelicula in peliculas:
        titulo, duracion, horarios_sub, horarios_dob = extraer_informacion(
            pelicula.full_text
        )
        if titulo != "Título no encontrado":
            print(
                f"Título: {titulo}, Duración: {duracion}, Horarios SUB: {horarios_sub}, Horarios DOB: {horarios_dob}"
            )


ubicaciones = ["moravia-costa-rica", "cartago-costa-rica"]
for ubicacion in ubicaciones:
    peliculas = obtener_peliculas_por_ubicacion(ubicacion)
    imprimir_informacion_peliculas(peliculas, ubicacion)



