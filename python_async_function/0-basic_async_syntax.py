#!/usr/bin/env python3
"sdfsdfds"


import asyncio
import random

async def wait_random(max_delay = 10):
    "sdfsdfds"
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
