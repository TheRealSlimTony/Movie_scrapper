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

def get_data_from_movies(movies, movie_schedules):
        movie_info = []
        for movie in movies:
            movie_data = {
                "Título": movie['name'],
                "Duración": movie['length'],
                "synopsis": movie['synopsis'],
                "genre": movie['genre'],
                "Imagen": f"https://static.cinepolis.com/img/peliculas/{movie['id']}/1/1/{movie['id']}.jpg",
                "video": f"https://static.cinepolis.com/videos/{movie['id']}/1/2/{movie['id']}.mp4",
                "Horarios": []
            }

            # Encuentra los horarios para la película actual
            schedule = next((s for s in movie_schedules if s['movie_id'] == movie['id']), None)
            if schedule:
                for date_info in schedule['dates']:
                    for format_info in date_info['formats']:
                        for showtime in format_info['showtimes']:
                            movie_data["Horarios"].append({
                                "Fecha": date_info['date'],
                                "Formato": format_info['language'],
                                "Hora": showtime['datetime'],
                                "Sala": showtime['screen']
                            })

            movie_info.append(movie_data)

        return (movie_info)


# imprimir_informacion_peliculas(movies, movie_schedules)

