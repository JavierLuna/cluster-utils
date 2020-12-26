#!/usr/bin/env python3
import json

from pyclusterlib.ssh import cluster_execute_ssh_command

COMMAND = "{ROOT}/hosts-info/get_host_info.py"

results = cluster_execute_ssh_command(COMMAND)

info = []
for stdout, stderr, exitcode in results:
    if stderr:
        info.append({"error": stderr})
    else:
        info.append(json.loads(stdout))


if __name__ == "__main__":
    print(json.dumps(info))
