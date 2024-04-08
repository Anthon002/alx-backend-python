#!/usr/bin/env python3
"""Testing module for utils.
"""
from typing import Dict, Tuple, Union
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock

from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """class for testing the access_nested_map function."""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int],
            ) -> None:
        """test method to test the output for access_nested_map """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            exception: Exception,
            ) -> None:
        """test method to test the exception for access_nested_map"""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """class for testing the get_json function"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(
            self,
            url_testing: str,
            test_payload: Dict,
            ) -> None:
        """method for testing output of  get_json """
        _attributes = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**_attributes)) as req_get:
            self.assertEqual(get_json(url_testing), test_payload)
            req_get.assert_called_once_with(url_testing)


class TestMemoize(unittest.TestCase):
    """Class for testing memoize """
    def test_memoize(self) -> None:
        """ method for testing memoize output """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(
                TestClass,
                "a_method",
                return_value=lambda: 42,
                ) as memoize_function_:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            memoize_function_.assert_called_once()
