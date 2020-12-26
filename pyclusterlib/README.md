# pyclusterlib

Utility library to execute commands within my Raspberry pi cluster.

## Installation

This library is not going to be published to PypI so your best bet is to install it as an editable package:

```
git clone https://github.com/JavierLuna/cluster-utils.git cluster-utils

cd cluster-utils/pyclusterlib

pip install -e .

```

That's it!

## Configuration

The following parameters can be modified by setting environment variables:

* `PYCLUSTERLIB_NODES_FILE_PATH`: Path to the `nodes.txt` file. Defaults to `~/cluster-utils/nodes.txt`.
* `PYCLUSTERLIB_THREAD_N`: Number of threads to use if work is paralellizable. Defaults to `4`.
