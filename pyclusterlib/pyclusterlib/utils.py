from functools import lru_cache

from pyclusterlib.config import NODES_FILE_PATH, CLUSTER_UTILS_ROOT

@lru_cache(maxsize=1)
def get_nodes():
    with open(NODES_FILE_PATH) as node_file:
        return [node.strip() for node in node_file if node.strip()]

def inject_variables(string: str) -> str:
    return string.format(ROOT=CLUSTER_UTILS_ROOT)

