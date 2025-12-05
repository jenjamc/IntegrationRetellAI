import multiprocessing

from admin_page import settings

workers_per_core = 2
cores = multiprocessing.cpu_count()
default_web_concurrency = workers_per_core * cores
web_concurrency = max(int(default_web_concurrency), 2)


# Gunicorn config variables
bind = f'0.0.0.0:{settings.PORT}'
workers = web_concurrency
graceful_timeout = 30
timeout = 6000
keepalive = 2
