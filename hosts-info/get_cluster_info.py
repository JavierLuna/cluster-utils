#!/usr/bin/env python3
import json

from pyclusterlib.ssh import cluster_execute_ssh_command
from pyclusterlib.config import CLUSTER_UTILS_ROOT as ROOT

COMMAND = f"{ROOT}/hosts-info/get_host_info.py"

def get_cluster_info():
    results = cluster_execute_ssh_command(COMMAND)

    info = []
    for stdout, stderr, exitcode in results:
        if stderr:
            info.append({"error": stderr})
        else:
            info.append(json.loads(stdout))
    return info


if __name__ == "__main__":
    print(json.dumps(get_cluster_info()))
