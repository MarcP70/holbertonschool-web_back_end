#!/usr/bin/env python3
"""
web.py
"""
import redis
import requests
from typing import Callable

# Redis connection
redis_client = redis.Redis()

def track_access(url: str) -> None:
    """
    Increment the count of how many times the URL has been accessed.

    Args:
        url (str): The URL to track.
    """
    redis_client.incr(f"count:{url}")

def cache_result(func: Callable) -> Callable:
    """
    Decorator to cache the result of a function call with an expiration time.

    Args:
        func (Callable): The function to be cached.

    Returns:
        Callable: The decorated function with caching functionality.
    """
    def wrapper(url: str) -> str:
        """
        Wrapped function to cache the result
        """
        cache_key = f"cache:{url}"

        # Check if the result is already in the cache
        cached_result = redis_client.get(cache_key)
        if cached_result:
            return cached_result.decode("utf-8")

        # Call the original function and cache the result
        result = func(url)
        redis_client.setex(cache_key, 10, result)
        return result

    return wrapper

@cache_result
def get_page(url: str) -> str:
    """
    Fetch the HTML content of the specified URL.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The HTML content of the URL.
    """
    # Track access to the URL
    track_access(url)

    # Fetch and return the HTML content
    response = requests.get(url)
    return response.text
