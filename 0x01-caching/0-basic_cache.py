#!/usr/bin/env python3
""" base_caching
"""
from base_caching import BaseCaching

class BasicCache(BaseCaching):

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key or item is None:
            exit()

        self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key.
        """
        return self.cache_data.get(key, None)
        

    

    
