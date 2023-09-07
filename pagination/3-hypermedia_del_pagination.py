#!/usr/bin/env python3
"""
Task 3: Deletion-resilient hypermedia pagination
"""
import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieve a page of data from a dataset based on the given index and
        page size.

        Args:
            index (int, optional): The starting index of the page to retrieve.
                Default is None.
            page_size (int, optional): The number of items to include in
                the page. Default is 10.

        Returns:
            dict: A dictionary containing the index, data, page size,
            and the next index for pagination purposes.
        """
        assert isinstance(index, int) and index >= 0

        indexed_dataset = self.indexed_dataset()

        if index >= len(self.dataset()):
            # If the index is outside the valid range, return an empty response
            return {
                'index': index,
                'data': [],
                'page_size': page_size,
                'next_index': None
            }

        # Get the data for the current page using the index
        data = [indexed_dataset.get(i, None) for i in
                range(index, index + page_size)]

        # Remove the None items (previously removed)
        data = [item for item in data if item is not None]

        next_index = index + page_size if len(data) > 0 else None

        response = {
            'index': index,
            'data': data,
            'page_size': page_size,
            'next_index': next_index
        }

        return response
