import shlex
import subprocess
import json
from typing import Union, List, Dict
from pprint import pprint
from multiprocessing.pool import ThreadPool as Pool

from pyclusterlib.utils import get_nodes
from pyclusterlib.config import THREAD_N

def execute_ssh_command(command: Union[str, List[str]]) -> dict:
    command = shlex.split(command) if isinstance(command, str) else command
    result = subprocess.run(command, capture_output=True)
    stdout, stderr = result.stdout.decode('utf-8'), result.stderr.decode('utf-8')
    return {"stdout": stdout, "stderr": stderr, "returncode": result.returncode}

def cluster_execute_ssh_command(command: Union[str, List[str]], include_this_host: bool=True) -> List[Dict[str, str]]:
    commands = [command] if include_this_host else []
    commands += [f"ssh {node} {command}" for node in get_nodes()]

    with Pool(min(len(commands), THREAD_N)) as pool:
        result = pool.map(execute_ssh_command, commands)
    return result
