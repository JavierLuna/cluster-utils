import shlex
import subprocess
import json
from typing import Union, List, Tuple
from multiprocessing.pool import ThreadPool as Pool

from pyclusterlib.utils import get_nodes
from pyclusterlib.config import THREAD_N


COMMAND_RESULT = Tuple[str, str, int]

def execute_command(command: str) -> COMMAND_RESULT:
    command = shlex.split(command)
    result = subprocess.run(command, capture_output=True)
    stdout, stderr = result.stdout.decode('utf-8'), result.stderr.decode('utf-8')
    return stdout, stderr, result.returncode


def execute_commands(commands: List[str]) -> List[COMMAND_RESULT]:
    with Pool(min(len(commands), THREAD_N)) as pool:
        result = pool.map(execute_command, commands)
    return result

