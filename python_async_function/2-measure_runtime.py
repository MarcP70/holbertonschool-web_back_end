#!/usr/bin/env python3
"""
Task 2:
Measures the average time it takes to execute the wait_n function.
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average time it takes to execute the wait_n function.

    Args:
        n (int): The number of coroutines to be executed.
        max_delay (int): The maximum delay for each coroutine.

    Returns:
        float: The average time taken to execute the coroutines.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
