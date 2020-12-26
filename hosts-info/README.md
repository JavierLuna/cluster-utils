# hosts-info

Get information of all the nodes in the cluster.

## Information

Information is outputed to `stdout` as a JSON string.
It has the following fields:

```json
{
    "hostname": "txema", // Host name
    "cpu_usage": [0.0, 1.0, 2.0, 0.0], // Usage percent per core
    "ram_usage": {
        "total": 8.0, // Total RAM in GB
        "available": 7.6, // Available RAM in GB
        "used": 0.4, // Used RAM in GB
        "percent": 0.05 // Percentage of used ram
    },
    "disk_usage": {
        "total": 64.0, // Total disk space in GB (total)
        "used": 3.2, // Used disk space in GB (total)
        "free": 60.0, // Free disk space in GB (user space)
        "percent": 0.01 // Percent of used space in GB (user space)
    },
    "cpu_temp": {"": 52.3} // Detected temperature data
}
```
