#!/usr/bin/env python3
'''implements LRUCache'''
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    '''
        LRUCache defines:
            defines a constant for the order of insertion
            put and get method for the cache
    '''
    def __init__(self):
        self.counts = {}
        self.count = -1
        super().__init__()

    def put(self, key, item):
        '''
            puts data to the cache with LRU replacement algorithm
        '''
        if len(self.cache_data) >= self.MAX_ITEMS and \
                key not in self.cache_data.keys():
            num = list(self.counts.keys).sort()[0]
            print(f'DISCARD: {self.counts[num]}')
            del self.cache_data[self.counts[num]]
            del self.counts[num]

        if not key or not item:
            return

        self.cache_data[key] = item

    def get(self, key):
        '''get data from cache data attribute by the key'''
        if key in self.cache_data.keys():
            self.count += 1
            self.counts[self.count] = key
        return self.cache_data.get(key, None)
