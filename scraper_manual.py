import re
from requests_html import HTMLSession
from bs4 import BeautifulSoup


def obtener_peliculas_por_ubicacion(ubicacion):
    session = HTMLSession()
    url = f"https://cinepolis.co.cr/cartelera/{ubicacion}/"
    r = session.get(url)
    r.html.render()
    return r.html.find("article")


def extraer_informacion(pelicula, html):
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
    soup = BeautifulSoup(html, "lxml")
    url_img = [img["src"] for img in soup.find_all("img") if "src" in img.attrs]

    sub_horarios_separados = re.findall(r"\d{2}:\d{2}", "".join(sub_horarios))
    dob_horarios_separados = re.findall(r"\d{2}:\d{2}", "".join(dob_horarios))

    return titulo, duracion, sub_horarios_separados, dob_horarios_separados, url_img


def imprimir_informacion_peliculas(peliculas, ubicacion):
    print(f"\nCartelera para: {ubicacion}")
    for pelicula in peliculas:
        titulo, duracion, horarios_sub, horarios_dob, url_img = extraer_informacion(
            pelicula.full_text, pelicula.html
        )
        if titulo != "Título no encontrado" and duracion != "Duración no encontrada":
            print(
                f"Título: {titulo}, Duración: {duracion}, Horarios SUB: {horarios_sub}, Horarios DOB: {horarios_dob}, Imagen: {url_img[0]}"
            )


def obtener_imagenes(peliculas, ubicacion):
    print(f"\nCartelera para: {ubicacion}")
    cartelera = []
    for pelicula in peliculas:
        titulo, duracion, horarios_sub, horarios_dob, url_img = extraer_informacion(
            pelicula.full_text, pelicula.html
        )
        if titulo != "Título no encontrado" and duracion != "Duración no encontrada":
            if titulo not in [peli["titulo"] for peli in cartelera]:
                pelicula_disponible = {"titulo": titulo, "url_img": url_img}
                cartelera.append(pelicula_disponible)
    return cartelera


# ubicaciones = ["moravia-costa-rica", "cartago-costa-rica"]
ubicaciones = ["moravia-costa-rica"]
for ubicacion in ubicaciones:
    peliculas = obtener_peliculas_por_ubicacion(ubicacion)
    # imprimir_informacion_peliculas(peliculas, ubicacion)
    obtener_imagenes(peliculas, ubicacion)
