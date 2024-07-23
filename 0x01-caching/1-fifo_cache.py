#!/usr/bin/env python3
'''implements FIFOCache'''
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''
        FIFOCache defines:
            defines a constant for the order of insertion
            put and get method for the cache
    '''
    def __init__(self):
        self.inserted_order = []
        super().__init__()

    def put(self, key, item):
        '''
            puts data to the cache with FIFO replacement algorithm
        '''
        if len(self.cache_data) >= self.MAX_ITEMS and \
                key not in self.cache_data.keys():
            print(f'DISCARD: {self.inserted_order[0]}')
            del self.cache_data[self.inserted_order[0]]
            self.inserted_order.pop(0)

        if not key or not item:
            return

        self.inserted_order.append(key)
        self.cache_data[key] = item

    def get(self, key):
        '''get data from cache data attribute by the key'''
        return self.cache_data.get(key, None)
