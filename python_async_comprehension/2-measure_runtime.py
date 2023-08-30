#!/usr/bin/env python3
"""
Task 2:
This module execute four coroutines in parallel,
measure the time and return it.
"""
import asyncio
import random
from typing import AsyncGenerator, List


async def async_generator() -> AsyncGenerator[float, None]:
    """
    An asynchronous generator that yields random numbers between 0 and 10
    at intervals of 1 second.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


async def async_comprehension() -> List[float]:
    """
    An asynchronous function that uses a list comprehension to iterate over
    the values yielded by the async_generator asynchronous generator and
    returns a list of those values.

    Returns:
        List[float]: A list of float values that are yielded by the
        async_generator asynchronous generator.
    """
    return [num async for num in async_generator()]


async def measure_runtime() -> float:
    """
    Measures the total runtime of four invocations of the async_comprehension
    function using the asyncio.gather function.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end_time = asyncio.get_event_loop().time()
    total_runtime = end_time - start_time
    return total_runtime
