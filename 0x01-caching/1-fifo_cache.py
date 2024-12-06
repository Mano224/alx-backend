#!/usr/bin/env python3
"""First-In First-Out caching module.
"""
from collections import OrderedDict
from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """First-In First-Out caching module.
    """
    def __init__(self):
        super().__init__()

        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key and item:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
             
            first_key = self.cache_data.popitem(last=False)
            print("DISCARD:", first_key)

    def get(self, key):
        """Retrieves an item by key.
        """
        self.cache_data.get(key, None)
