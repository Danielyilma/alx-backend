#!/usr/bin/env python3
'''implemant a sever class that handles data pagination'''
import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''return page by accepting page number and its range'''

        self.dataset()
        assert type(page) is int and page > 0, "page must be postive"
        assert type(page_size) is int and page_size > 0, "page must be postive"

        page_range = self.index_range(page, page_size)
        data_length = len(self.__dataset)
        if page_range[0] >= data_length or page_range[1] >= data_length:
            return []

        return self.__dataset[page_range[0]:page_range[1]]

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        '''returns the starting and end index of a page'''
        start_index = (page - 1) * page_size
        return (start_index, start_index + page_size)

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''return a dict that includes info about current page and the page'''
        page_data = {'page': page, 'data': self.get_page(page, page_size)}
        page_length = len(self.__dataset)
        page_data['total_pages'] = math.ceil(page_length / page_size)
        page_data['page_size'] = len(page_data['data'])

        page_range = self.index_range(page, page_size)
        page_data['next_page'] = page + 1 if page_range[1] <= page_length\
            else None
        page_data['prev_page'] = page - 1 if page_range[0] > 0 else None

        return page_data
