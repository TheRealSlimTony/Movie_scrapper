import multiprocessing
import os

# El socket a vincular. Un `(host, puerto)` o `(dirección, puerto)` o una cadena de `unix:path`.
# Se puede especificar múltiples veces. Ejemplo: ['0.0.0.0:8000']
# bind = "0.0.0.0:8000"

port = os.getenv("PORT", 8000)
bind = f"0.0.0.0:{port}"

# El número de procesos de trabajo que se deben ejecutar.
# Una buena base de partida es `(2 x $num_cores) + 1`.
workers = multiprocessing.cpu_count() * 2 + 1

# El número de hilos de trabajo para manejar las solicitudes.
# Normalmente se establece entre 2-4 por worker.
threads = 2

# El nivel de los logs. Los niveles disponibles incluyen debug, info, warning, error, y critical.
loglevel = 'info'

# La clase de worker a utilizar. Para aplicaciones FastAPI (ASGI), se utiliza UvicornWorker.
worker_class = "uvicorn.workers.UvicornWorker"

# Tiempo máximo en segundos para esperar a que un worker responda.
timeout = 120

# Tiempo máximo en segundos para esperar antes de reiniciar un worker.
graceful_timeout = 120

# El archivo donde se guardarán los logs de error.
errorlog = '-'

# El archivo donde se guardarán los logs de acceso.
accesslog = '-'

# Formato para los logs de acceso.
# Puedes personalizarlo para incluir la información que consideres relevante.
access_log_format = '%({X-Forwarded-For}i)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

