#!/usr/bin/env python3

"""
This module provides a unit test for the access_nested_map function.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case for access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Test access_nested_map function.

        Args:
            nested_map (dict): The nested map to access.
            path (tuple): The path to follow in the nested map.
            expected_result: The expected result.

        Returns:
            None.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)
