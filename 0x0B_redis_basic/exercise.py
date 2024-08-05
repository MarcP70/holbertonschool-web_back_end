#!/usr/bin/env python3
"""
Writing strings to Redis.
"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count how many times a method is called.
    """
    # Generate a key based on the qualified name of the method
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args):
        """
        Increment the call count for this key in Redis
        """
        self._redis.incr(key)

        # Call the original method and return its result
        return method(self, *args)
    return wrapper

class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generate a random key, store the input data in Redis using the random
            key and return the key.
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable[[bytes], any]] = None) -> Optional[any]:
        """
        Retrieve the value from Redis using the provided key and optionally
            apply a conversion function.
        """
        value = self._redis.get(key)
        if not value:
            return None

        if fn:
            value = fn(value)

        return value

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve the value from Redis using the provided key and convert it
            to a string.
        """
        return self.get(key, fn=lambda value: value.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve the value from Redis using the provided key and convert it to
            an integer.
        """
        return self.get(key, fn=int)
