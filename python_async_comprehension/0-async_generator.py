#!/usr/bin/env python3
"""
Async Generator
"""


import asyncio
import random
import typing
from types import NoneType


async def async_generator() -> typing.Generator[float, NoneType, NoneType]:
    """Async Generator function that takes no arguments"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
