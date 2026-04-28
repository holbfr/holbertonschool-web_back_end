#!/usr/bin/env python3
"""
Concurrent coroutines example.
"""


import asyncio
import typing
wait_n = __import__('1-concurrent_coroutines').wait_n
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> typing.List[float]:
    """Wait for n random delays and return them as a list in ASC order."""
    delays = [task_wait_random(max_delay) for _ in range(n)]
    result = await asyncio.gather(*delays)
    return sorted(result)
