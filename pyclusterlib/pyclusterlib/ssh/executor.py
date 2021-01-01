import shlex
import subprocess
import json
from typing import Tuple, List
from pprint import pprint
from multiprocessing.pool import ThreadPool as Pool

from pyclusterlib.utils import expand_multinode_command
from pyclusterlib.config import THREAD_N
from pyclusterlib.cmd.executor import execute_commands, COMMAND_RESULT


def cluster_execute_ssh_command(command: str, include_this_host: bool=True) -> List[COMMAND_RESULT]:
    commands = [command] if include_this_host else []
    commands += expand_multinode_command("ssh {NODE} " + command)

    return execute_commands(commands)
