#!/usr/bin/env python3
"""Parameterize a unit test
   Mock HTTP calls
   Parameterize and patch
"""

import unittest
from parameterized import parameterized  # type: ignore
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """A class Created to parameterized a unit test."""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)])
    def test_access_nested_map(self, nested_map, path, expected):
        """A method to test the nested map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")])
    def test_access_nested_map_exception(self, nested_map, path, expeted_erro):
        """A method to test the nested map"""
        with self.assertRaises(KeyError) as key_error:
            access_nested_map(nested_map, path)
            nest_exception = key_error.exception
            self.assertEqual(expeted_erro, nest_exception)


class TestGetJson(unittest.TestCase):
    """A class to mock HTTP calls."""
    @parameterized.expand([
        "http://example.com", {"payload": True},
        "http://holberton.io", {"payload": False}])
    @patch('utils.get_json')
    def test_get_json(self, test_url, test_payload):
        """A method that works well with get_json."""
        # configure the value returned by calling the mock with Mock class:
        mock_cls = Mock()
        mock_cls.json.return_value = test_payload
        with patch('request.get', return_value=mock_cls):
            res = get_json(test_url)
            # Test that the mocked get method was called exactly once
            # (per input) with test_urls as argument.
            mock_cls.json.assert_called_once()
            # Test that the output of get_json is equak to test_payload
            self.assertEqual(res, test_payload)


class TestMemoize(unittest.TestCase):
    """Parameterize and patch."""
    def test_memorize(self):
        """A method to test the function memorize."""
        class TestClass:
            """A class underneath a class."""

            def a_method(self):
                """A method underneath a class."""
                return 42

            @memorize  # type: ignore
            def a_property(self):
                """A Second method underneath a class."""
                return self.a_method()

        with patch.object(TestClass,
                          'a_method', return_value=42) as mock_method:
            product_cls = TestClass()
            product_cls.a_property
            product_cls.a_property
            mock_method.assert_called_once()
