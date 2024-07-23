#!/usr/bin/env python3
'''implementing BasicCache class'''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''
        BasicCache class that inherit from BaseCaching
        it implement methods :
            put : adds key : value to the cache
            get : gets data from the cache
    '''
    def put(self, key, item):
        '''add data to the cache_data attribute'''
        if not key or not item:
            return

        self.cache_data[key] = item

    def get(self, key):
        '''get data from cache data attribute by the key'''
        return self.cache_data.get(key, None)
