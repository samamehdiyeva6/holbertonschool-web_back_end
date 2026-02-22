#!/usr/bin/python3
"""Async comprehension that collects 10 random numbers using an async generator."""

async_generator = __import__('0-async_generator').async_generator
import asyncio
from typing import Generator, List


async def async_comprehension() -> Generator[None, None, List[float]]:
    """Collect 10 random numbers using an async generator."""
    return [i async for i in async_generator()]
