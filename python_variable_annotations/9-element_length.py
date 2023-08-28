#!/usr/bin/env python3
"""
Task 9:
Returns a list of tuples, where each tuple contains a sequence from
        the input list and its corresponding length.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, where each tuple contains a sequence from
        the input list and its corresponding length.

    Args:
        lst (Iterable[Sequence]): A list of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, where each tuple contains
            a sequence from the input list and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
