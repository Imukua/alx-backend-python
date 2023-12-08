#!/usr/bin/env python3
"""make_multiplier
"""


import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """Return function that multiplies float by multiplier"""
    def float_multiply(x: float) -> float:
        return multiplier * x

    return float_multiply
