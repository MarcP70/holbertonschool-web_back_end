#!/usr/bin/env python3
"""
Task 4:
Asynchronously executes a given number of tasks with a maximum delay
for each task.
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously executes a given number of tasks with a maximum delay
    for each task.

    Args:
        n (int): The number of tasks to be executed.
        max_delay (int): The maximum delay for each task.

    Returns:
        List[float]: A list of floats representing the delays of each task.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return delays
