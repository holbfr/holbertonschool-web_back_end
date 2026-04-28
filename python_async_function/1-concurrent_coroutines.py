#!/usr/bin/env python3
"""
Concurrent coroutines example.
"""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> list[float]:
    """Wait for n random delays and return them as a list in ASC order."""
    delays = [wait_random(max_delay) for _ in range(n)]
    result = await asyncio.gather(*delays)
    return sorted(result)
