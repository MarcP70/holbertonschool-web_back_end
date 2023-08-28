#!/usr/bin/env python3
"""
Task 8:
Returns a function that multiplies a float value by the provided multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float value by the
        provided multiplier.

    Args:
        multiplier (float): The factor by which the input value
            will be multiplied.

    Returns:
        Callable[[float], float]: A closure that takes a float value as input
            and returns the result of multiplying it by the multiplier.
    """
    def multiplier_function(value: float) -> float:
        """
        Returns the result of multiplying the input value by the multiplier.

        :param value: The float value to be multiplied.
        :return: The result of multiplying the input value by the multiplier.
        """
        return value * multiplier

    return multiplier_function
