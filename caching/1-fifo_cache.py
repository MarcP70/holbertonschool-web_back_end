#!/usr/bin//env python3
""" FIFOCache module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache defines:
      - caching system using FIFO algorithm
    """

    def __init__(self):
        """ Initialize the FIFOCache
        """
        super().__init__()

    def put(self, key, item):
        """ Add or update an item in the cache
        """
        if key is None or item is None:
            return

        # If the key already exists, remove it from the cache
        if key in self.cache_data:
            del self.cache_data[key]

        # If the cache is full, discard the first item (FIFO)
        if len(self.cache_data) >= self.MAX_ITEMS:
            discarded_key = next(iter(self.cache_data))
            del self.cache_data[discarded_key]
            print("DISCARD:", discarded_key)

        self.cache_data[key] = item  # Add the item to the cache

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
