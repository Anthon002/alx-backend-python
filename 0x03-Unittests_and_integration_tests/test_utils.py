#!usr/bin/env python3
""" module for testing the utils
"""
from utils import access_nested_map
import unittest
from typing import Dict, Tuple, Union
from parameterized import parameterized

class TestAccessNestedMap(unittest.TestCase):
    """Class to test access_nested_map """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            path: Tuple[str],
            nested_map: Dict,
            expected: Union[Dict, int],
            ) -> None:
        """method to test output of access_nested_map """
        self.assertEqual(access_nested_map(nested_map, path), expected)
