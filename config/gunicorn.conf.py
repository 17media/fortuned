# -*- coding: utf-8 -*-
import multiprocessing
import os


workers = int(os.environ.get('GUNICORN_WORKERS') or (2 * multiprocessing.cpu_count()))
worker_class = os.environ.get('GUNICORN_WORKER_CLASS') or 'aiohttp.worker.GunicornWebWorker'
loglevel = os.environ.get('GUNICORN_LOGLEVEL') or 'info'
accesslog = '-'
errorlog = '-'
forwarded_allow_ips = '*'
secure_scheme_headers = {
    # 'X-FORWARDED-PROTOCOL': 'ssl',
    'X-FORWARDED-PROTO': 'https',
    # 'X-FORWARDED-SSL': 'on',
}
# preload_app = True
# limit_request_line = int(4094 / 4)
# limit_request_fields = int(100 / 2)
# keepalive = 2 * 2
