# Cluster utils

Set of scripts to manage my Raspberry Pi cluster. They are supposed to run in the primary node.

## Setup

Clone this repository in each of the nodes of the cluster (primary too):

```
git clone git@github.com:JavierLuna/cluster-utils.git ~/cluster-utils 
```

Some of the scripts expect a `nodes.txt` file in the root of this directory, containing all the worker nodes in the cluster.

`nodes.txt` example:

```
node1
pi@node2
pi@192.168.0.3
```

Each of the scripts may have dependencies you need to install. I'm working on a script to install everything at once and keep the nodes updated.

## Utilities

* `hosts-info`: Gather useful information from all the nodes, like CPU/RAM/Disk usage, hostnames, temperatures...
