#!/usr/bin/env python3
"""
Task 3:
Create an asyncio task that waits for a random amount of time.
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio task that waits for a random amount of time.

    :param max_delay: An integer representing the maximum delay in seconds.
    :return: An asyncio task object that can be awaited or
        scheduled for execution.
    """
    coroutine_time = wait_random(max_delay)
    coroutine_task = asyncio.create_task(coroutine_time)
    return coroutine_task
