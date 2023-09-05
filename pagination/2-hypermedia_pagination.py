#!/usr/bin/env python3
"""
Task 2.
"""
import csv
import math
from typing import List, Dict


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


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a specific page of data from a dataset.

        Args:
            page (int, optional):
                The page number to retrieve (default is 1).
            page_size (int, optional):
                The number of items per page (default is 10).

        Returns:
            List[List]: The subset of data corresponding to the requested page.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        dataset = self.dataset()

        if start >= len(dataset):
            return []

        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Retrieve a specific page of data from a dataset and return it along
        with additional information for pagination purposes.

        Args:
            page (int, optional):
                The page number to retrieve (default is 1).
            page_size (int, optional):
                The number of items per page (default is 10).

        Returns:
            dict: A dictionary containing information about the retrieved page
            of data and pagination details.
                - 'page_size': The number of items in the retrieved page.
                - 'page': The current page number.
                - 'data': The retrieved page data.
                - 'next_page': The next page number if it exists,
                otherwise None.
                - 'prev_page': The previous page number if it exists,
                otherwise None.
                - 'total_pages': The total number of pages.
        """
        page_data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        hypermedia = {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }

        return hypermedia
