import socket
import os
from timeit import default_timer as timer

import psutil
from flask import Flask

TO_GB = 1024 ** 3
CACHE_TTL_SECONDS = 5

cached_since = None
cached_stats = None

app = Flask(__name__)

def get_host_stats():
    global cached_since, cached_stats

    if cached_stats and cached_since and CACHE_TTL_SECONDS < timer() - cached_since:
        return cached_stats

    cpu_usage = psutil.cpu_percent(interval=1, percpu=True)
    ram_usage = psutil.virtual_memory()
    disk_usage = psutil.disk_usage('/')
    try:
        temps = {temp.label: temp.current for temp in psutil.sensors_temperatures()["cpu_thermal"]}
    except:
        temps = "??"

    cached_stats = {
        "hostname": os.getenv("HOST_NAME", socket.gethostname()),
        "cpu_usage": cpu_usage,
        "ram_usage": {
            "total": ram_usage.total / TO_GB,
            "available": ram_usage.available / TO_GB,
            "used": ram_usage.used / TO_GB,
            "percent": ram_usage.percent
        },
        "disk_usage": {
            "total": disk_usage.total / TO_GB,
            "used": disk_usage.used / TO_GB,
            "free": disk_usage.free / TO_GB,
            "percent": disk_usage.percent
        },
        "cpu_temp": temps
    }

    cached_since = timer()
    return cached_stats


@app.route("/")
def get_host_info():
    return get_host_stats()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
