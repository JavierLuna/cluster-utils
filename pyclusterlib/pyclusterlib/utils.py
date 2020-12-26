from functools import lru_cache

from pyclusterlib.config import NODES_FILE_PATH

@lru_cache(maxsize=1)
def get_nodes():
    with open(NODES_FILE_PATH) as node_file:
        return [node.strip() for node in node_file if node.strip()]

