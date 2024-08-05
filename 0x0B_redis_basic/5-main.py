#!/usr/bin/env python3
"""
test_web.py
"""
from web import get_page

# Test with an alternative slow response URL
url = "http://httpbin.org/delay/10"

# Fetch the page content
print(get_page(url))

# Fetch again to see caching in effect
print(get_page(url))

# Check access count
import redis
redis_client = redis.Redis()
print(redis_client.get(f"count:{url}").decode("utf-8"))
