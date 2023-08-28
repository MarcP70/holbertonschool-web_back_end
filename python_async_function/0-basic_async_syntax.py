#!/usr/bin/env python3
"""
Task 0:
Generates a random delay and then waits for that delay.
"""
import asyncio
import random


async def wait_random(max_delay=10):
    """
    Generates a random delay and then waits for that delay.

    :param max_delay: The maximum delay in seconds. Default is 10 seconds.
    :type max_delay: float
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
