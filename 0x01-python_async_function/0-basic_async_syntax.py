#!/usr/bin/env python3
# 0-basic_async_syntax.py - The basics of async

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """"""
    i = random.randrange(0, 10) 
    await asyncio.sleep(i)
    return i
