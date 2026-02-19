#!/usr/bin/env python3
"""sdfsdfdsfsd"""


import asyncio
import random


async def async_generator():
    """"sdfsdfsd"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.randrange(0,10)
