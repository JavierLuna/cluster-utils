#!/usr/bin/env python3
import shlex
import subprocess
import json
from pprint import pprint
from multiprocessing.pool import ThreadPool as Pool

NODES_FILE = "../nodes.txt"
INCLUDE_SELF_INFO = True

with open(NODES_FILE) as nodes_file:
    nodes = [node.strip() for node in nodes_file if node.strip()]

commands = ["./get_host_info.py"] if INCLUDE_SELF_INFO else []


commands += [f"ssh {node} ~/cluster-utils/hosts-info/get_host_info.py" for node in nodes]

def get_info(command: str) -> dict:
    result = subprocess.run(shlex.split(command), capture_output=True)
    stdout, stderr = result.stdout.decode('utf-8'), result.stderr.decode('utf-8')
    if stderr:
        node_info = {"error": stderr, "command": command}
    else:
        node_info = json.loads(stdout)
    return {"hostname": node_info.get("hostname", "ERROR"), "node_info": node_info}


with Pool(len(commands)) as p:
    infos = p.map(get_info, commands)

if __name__ == "__main__":
    print(json.dumps(infos))
