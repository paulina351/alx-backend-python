#!/usr/bin/env python3
"""# 1-concurrent_coroutines.py - Let's execute multiple
# coroutines at the same time with async
"""

from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """The list of the delays should be in ascending
        order without using sort() because of concurrency.
    """
    a = [wait_random(max_delay) for _ in range(n)]
    a = asyncio.as_completed(a)
    delays = [await b for b in a]
    return delays
