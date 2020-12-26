#!/usr/bin/env python3
import json
import psutil
import socket

TO_GB = 1024 ** 3

cpu_usage = psutil.cpu_percent(interval=1, percpu=True)
ram_usage = psutil.virtual_memory()
disk_usage = psutil.disk_usage('/')
temps = psutil.sensors_temperatures()["cpu_thermal"]

node_info = {
    "hostname": socket.gethostname(),
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
    "cpu_temp": {temp.label: temp.current for temp in temps}
}

str_node_info = json.dumps(node_info)

if __name__ == "__main__":
    print(str_node_info)
