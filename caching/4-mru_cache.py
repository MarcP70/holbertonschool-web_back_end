#!/usr/bin//env python3
""" MRUCache module
"""

from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache defines:
      - caching system using MRU algorithm
    """

    def __init__(self):
        """ Initialize the MRUCache
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add or update an item in the cache
        """
        if key is None or item is None:
            return

        # If the key already exists, move it to the end (most recently used)
        if key in self.cache_data:
            del self.cache_data[key]
        elif len(self.cache_data) >= self.MAX_ITEMS:
            # If the cache is full, discard the most recently used item
            discarded_key, _ = self.cache_data.popitem(last=True)
            print("DISCARD:", discarded_key)

        self.cache_data[key] = item  # Add or update the item

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed item to the end (most recently used)
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
