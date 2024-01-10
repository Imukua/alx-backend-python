#!/usr/bin/env python3
"""
Testing utils.py file
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock

class TestAccessNestedMap(unittest.TestCase):
    """
    tests access nested map function
    """

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)
        ]
    )
    def test_access_nested_map(self, nested_map, path, expectedoutput):
        """
        test_access_nested_map
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expectedoutput)

    @parameterized.expand(
        [
            ({}, ("a",), KeyError),
            ({"a": 1}, ("a", "b"), KeyError)
        ]
    )
    def test_access_nested_map_exception(self, nested_map, path,
                                         expectedoutput):
        """
        test_access_nested_map_exception
        """
        with self.assertRaises(expectedoutput) as context:
            access_nested_map(nested_map, path)
