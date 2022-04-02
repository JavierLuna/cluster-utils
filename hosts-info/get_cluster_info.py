#!/usr/bin/env python3
import asyncio
from typing import List
from config import NODES_TXT_PATH

import aiohttp


def get_node_names() -> List[str]:
    with open(NODES_TXT_PATH) as nodes_txt_file:
        return [l.strip() for l in nodes_txt_file]


async def get(url, session: aiohttp.ClientSession):
    try:
        async with session.get(url=url) as response:
            resp = await response.json()
        return resp
    except Exception as e:
        print("Unable to get url {} due to {}.".format(url, e.__class__))


async def get_cluster_info(node_names: List[str]):
    async with aiohttp.ClientSession() as session:
        ret = await asyncio.gather(*[get(f"http://{node_name}:5000", session) for node_name in node_names])
    return ret


if __name__ == "__main__":
    print(asyncio.run(get_cluster_info(get_node_names())))
