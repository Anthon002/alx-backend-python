#!usr/bin/env python3
""" module for testing the utils
"""
from utils import access_nested_map
import unittest
from typing import Dict, Tuple, Union

class TestAccessNestedMap(unittest.TestCase):
    """
    Class
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])

    def
