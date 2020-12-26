import os

NODES_FILE_PATH = os.getenv("PYCLUSTERLIB_NODES_FILE_PATH", "~/cluster-utils/nodes.txt")
THREAD_N = int(os.getenv("PYCLUSTERLIB_THREAD_N", 4))
