#!/usr/bin/env python3
"""least_recently_used caching module.
"""
from collections import OrderedDict

from base_caching import BaseCaching

class LRUCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary with a LRU
    algorithm when the limit is reached.
    """
    def __init__(self):
        """Initializes the cache.
        """
        super.__init__()

        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if not key and item:
            return
        if len(self.cache_data) +1 > BaseCaching.MAX_ITEMS:
            LRU_ITEM, _ = self.cache_data.popitem(last=False)
            print("DISCARD:", LRU_ITEM)
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key.
        """
        return self.cache_data[key, None]
