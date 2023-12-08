#!/usr/bin/env python3
"""to_kv
"""


import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """returns  tuple of  string & square  v as float"""
    return (k, float(v * v))
