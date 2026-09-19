#!/usr/bin/env python3
"""Simple helper function for pagination"""


def index_range(page, page_size):
    """Return a tuple of start and end index for a given page and page_size"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
