import os

dir_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

CLUSTER_UTILS_ROOT = os.getenv("PYCLUSTERLIB_CLUSTER_UTILS_ROOT",os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
NODES_FILE_PATH = os.getenv("PYCLUSTERLIB_NODES_FILE_PATH", os.path.join(CLUSTER_UTILS_ROOT, "nodes.txt"))
THREAD_N = int(os.getenv("PYCLUSTERLIB_THREAD_N", 4))
