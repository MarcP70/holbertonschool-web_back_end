#!/usr/bin/env python3
"""
Task 1:
An asynchronous function called `async_comprehension` that uses a list
comprehension to iterate over the values yielded by the `async_generator`
asynchronous generator and returns a list of those values.
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
