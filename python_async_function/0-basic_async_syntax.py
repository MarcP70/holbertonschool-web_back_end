#!/usr/bin/env python3
"""
Task 0:
Generates a random delay and then waits for that delay.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Generates a random delay and then waits for that delay.

    Args:
        max_delay (Union[int, float]): The maximum delay in seconds.
        Default is 10.

    Returns:
        float: The random delay that was waited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
