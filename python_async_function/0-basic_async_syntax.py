#!/usr/bin/env python3
"""
Simple example of async syntax in Python.
"""




async def wait_random(max_delay = 10):
    """Wait for a random delay between 0 and max_delay seconds."""
    import random
    import asyncio

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
