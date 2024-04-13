import json
import requests

def get_data_from_cinema_id(cinema_id):
    reqUrl = f"https://cinepolis.co.cr/api/schedule_cinema?cinema_id={cinema_id}"
    headersList = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd"
}
    payload = ""
    response = requests.get(reqUrl, headers=headersList)

    data = response.json()
    return data

# data = get_data_from_cinema_id()

# movies = data['schedules']['movies']
# movie_schedules = data['schedules']['schedules']

def imprimir_informacion_peliculas(movies, movie_schedules):
    for movie in movies:
        print(f"Título: {movie['name']}")
        print(f"Duración: {movie['length']}")
        print(f"Imagen: https://static.cinepolis.com/img/peliculas/{movie['id']}/1/1/{movie['id']}.jpg")

        # Encuentra los horarios para la película actual
        schedule = next((s for s in movie_schedules if s['movie_id'] == movie['id']), None)
        if schedule:
            print("Horarios:")
            for date_info in schedule['dates']:
                print(f"  Fecha: {date_info['date']}")
                for format_info in date_info['formats']:
                    print(f"    Formato: {format_info['language']}")
                    for showtime in format_info['showtimes']:
                        print(f"      Hora: {showtime['datetime']} en Sala {showtime['screen']}")
        print("-" * 40)  # Separador para la siguiente película


# imprimir_informacion_peliculas(movies, movie_schedules)
