#!/usr/bin/env python3
"""
Task 0.
"""


def index_range(page, page_size):
    """
    Return a tuple of start and end indexes for a given page and page_size.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start and end indexes for the page.
    """
    if page <= 0 or page_size <= 0:
        return (0, 0)

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)
