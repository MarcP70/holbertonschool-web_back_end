#!/usr/bin/env python3
"""
Task 7:
Returns a tuple containing the key and the square of the value.
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple containing the key and the square of the value.

    Args:
        k (str): A string representing the key.
        v (Union[int, float]): A value of type `Union[int, float]`
            which can be either an integer or a float.

    Returns:
        Tuple[str, float]: A tuple containing the key and the
            square of the value.
    """
    return (k, v ** 2)
