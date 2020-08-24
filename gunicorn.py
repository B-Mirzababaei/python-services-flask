from multiprocessing import cpu_count

bind = '0.0.0.0:8030'
# daemon = True
# workers = cpu_count()
workers = 4
timeout = 240
max_requests = 100
worker_class = 'gevent'
