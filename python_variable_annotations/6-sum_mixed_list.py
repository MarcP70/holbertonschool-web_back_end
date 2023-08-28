#!/usr/bin/env python3
"""
Rask 6:
Calculate the sum of all the elements in a list of integers and floats.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of all the elements in a list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list of integers and floats.

    Returns:
        float: The sum of all the elements in the input list.
    """
    return sum(mxd_lst)
