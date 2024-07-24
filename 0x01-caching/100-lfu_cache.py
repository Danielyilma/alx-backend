#!/usr/bin/env python3
'''implements LFUCache'''
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    '''
        LFUCache defines:
            defines a constant for the order of insertion
            put and get method for the cache
    '''
    def __init__(self):
        '''initialize attributes'''
        # holds tuple of key and frequncy usage
        self.data_count = []
        # counter
        self.count = -1

        super().__init__()

    def put(self, key, item):
        '''
            puts data to the cache with LFU replacement algorithm
        '''
        if not key and not item:
            return
        # checking if the cache is full
        if len(self.cache_data) >= self.MAX_ITEMS \
                and key not in self.cache_data.keys():

            self.data_count.sort(key=lambda x: x[1])
            least_count = self.data_count[0]
            index, least_ordered = 0, least_count[2]
            for i, value in enumerate(self.data_count):
                if value[1] != least_count[1]:
                    break

                if least_ordered > value[2]:
                    least_ordered = value[2]
                    index = i

            print(f"DISCARD: {self.data_count[index][0]}")
            del self.cache_data[self.data_count[index][0]]
            self.data_count.pop(index)
        # checking if the cache is full and the key to
        # be added is already in the cache
        elif key in self.cache_data.keys():
            for i, value in enumerate(self.data_count):
                if value[0] == key:
                    self.count += 1
                    self.data_count[i] = (
                        key, self.data_count[i][1] + 1, self.count
                    )

            self.cache_data[key] = item
            return
        # adding the key, count frequency and usage order to a list
        self.count += 1
        self.data_count.append((key, 0, self.count))
        self.cache_data[key] = item

    def get(self, key):
        '''get data from cache data attribute by the key'''
        if key not in self.cache_data.keys():
            return None

        for i, item in enumerate(self.data_count):
            if item[0] == key:
                self.count += 1
                self.data_count[i] = (
                    key, self.data_count[i][1] + 1, self.count
                )

        return (self.cache_data.get(key))
