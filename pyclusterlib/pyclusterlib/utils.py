from functools import lru_cache
from typing import List

from pyclusterlib.config import NODES_FILE_PATH

@lru_cache(maxsize=1)
def get_nodes():
    with open(NODES_FILE_PATH) as node_file:
        return [node.strip() for node in node_file if node.strip()]

    return string.format(ROOT=CLUSTER_UTILS_ROOT)

def expand_multinode_command(command: str) -> List[str]:
    return [command.format(NODE=node) for node in get_nodes()]
