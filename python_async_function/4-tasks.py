#!/usr/bin/env python3
"sdfsdfds"


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_n(n: int, max_delay: int) -> List[float]:
    """sdfds"""
    tasks = [asyncio.run(wait_random(max_delay)) for _ in range(n)]

    delays = []
    for completed in asyncio.as_completed(tasks):
        delays.append(completed)

    return delays
