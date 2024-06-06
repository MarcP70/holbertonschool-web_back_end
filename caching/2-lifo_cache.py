#!/usr/bin//env python3
""" LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache defines:
      - caching system using LIFO algorithm
    """

    def __init__(self):
        """ Initialize the LIFOCache
        """
        super().__init__()

    def put(self, key, item):
        """ Add or update an item in the cache
        """
        if key is None or item is None:
            return

        # If the key already exists, update its value and move it to the end
        if key in self.cache_data:
            # Remove the key from its current position
            del self.cache_data[key]
        elif len(self.cache_data) >= self.MAX_ITEMS:
            # If the cache is full, discard the last item (LIFO)
            discarded_key = list(self.cache_data.keys())[-1]
            del self.cache_data[discarded_key]
            print("DISCARD:", discarded_key)

        self.cache_data[key] = item  # Add or update the item

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
