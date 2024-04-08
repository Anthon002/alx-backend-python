#!usr/bin/env python3
""" module for testing the utils
"""
from utils import access_nested_map
import unittest
from typing import Dict, Tuple, Union

class TestAccessNestedMap(unittest.TestCase):
    """
    Class to test the access_nested_map function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])

    def test_access_nested_map(self, path: Tuple(str), expected: Union[Dict, int], nested_map: Dict):
        """Method to test Output access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
