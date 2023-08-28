#!/usr/bin/env python3
"""
Task 1:
Spawn wait_random n times with specified max_delay and
    returns list of all the delays.
"""
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns wait_random n times
        with specified max_delay.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay for wait_random.

    Returns:
        List[float]: List of all the delays (float values).
    """
    delays = [await wait_random(max_delay) for _ in range(n)]
    return sorted(delays)
