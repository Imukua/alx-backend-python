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

class TestGetJson(unittest.TestCase):
    """
    tests get json function
    """
    @parameterized.expand(
        [
            ('http://example.com', {'payload': True}),
            ('http://holberton.io', {'payload': False})
        ]
    )
    def test_get_json(self, url, expectedoutput):
        """
        tests get json
        """
        mock_response = Mock()
        mock_response.json.return_value = expectedoutput
        with patch('requests.get', return_value=mock_response):
            response = get_json(url)

            self.assertEqual(response, expectedoutput)

class TestMemoize(unittest.TestCase):
    """
    test memoize
    """

    def test_memoize(self):
        """
        tests memoize
        """

        class TestClass:
            """
            test class
            """

            def a_method(self):
                """
                returns 42
                """
                return 42

            @memoize
            def a_property(self):
                """
                returns the a_method
                """
                return self.a_method()

        test_obj = TestClass()

        with patch.object(test_obj, 'a_method') as mock_method:
            mock_method.return_value = 42

            result1 = test_obj.a_property
            result2 = test_obj.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()
