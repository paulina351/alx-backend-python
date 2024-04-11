#!/usr/bin/env python3
"""# Measure the runtime"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n, max_delay) -> float:
    """Create a measure_time function with integers n and
        max_delay as arguments that measures the total
        execution time for wait_n(n, max_delay), and
        returns total_time / n. Your function should return a float.
    """
    begin_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    return (end_time - begin_time) / n
