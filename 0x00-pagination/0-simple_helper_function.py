#!/usr/bin/env python3
'''a module that implemets helper function index_range'''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''returns the starting and end index of a page'''
    start_index = (page - 1) * page_size
    return (start_index, start_index + page_size)
