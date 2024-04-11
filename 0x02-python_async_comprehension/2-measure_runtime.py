#!/usr/bin/env python3
"""Run time for four parallel comprehensions
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """write a measure_runtime coroutine that will
        execute async_comprehension four times in
        parallel using asyncio.gather.
    """
    begin_time = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    return time.perf_counter() - begin_time
