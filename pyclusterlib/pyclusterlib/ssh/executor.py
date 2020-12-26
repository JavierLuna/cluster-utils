import shlex
import subprocess
import json
from typing import Union, List, Dict, Tuple
from pprint import pprint
from multiprocessing.pool import ThreadPool as Pool

from pyclusterlib.utils import get_nodes, inject_variables
from pyclusterlib.config import THREAD_N

REMOTE_COMMAND_RESULT = Tuple[str, str, int]

def execute_ssh_command(command: Union[str, List[str]]) -> REMOTE_COMMAND_RESULT:
    command = shlex.split(command) if isinstance(command, str) else command
    command = [inject_variables(c) for c in command]
    result = subprocess.run(command, capture_output=True)
    stdout, stderr = result.stdout.decode('utf-8'), result.stderr.decode('utf-8')
    return stdout, stderr, result.returncode

def cluster_execute_ssh_command(command: Union[str, List[str]], include_this_host: bool=True) -> List[REMOTE_COMMAND_RESULT]:
    commands = [command] if include_this_host else []
    commands += [f"ssh {node} {command}" for node in get_nodes()]

    with Pool(min(len(commands), THREAD_N)) as pool:
        result = pool.map(execute_ssh_command, commands)
    return result
