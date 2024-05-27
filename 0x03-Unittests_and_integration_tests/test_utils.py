#!/usr/bin/env python3
"""Parameterize a unit test
   Mock HTTP calls
   Parameterize and patch
"""

import unittest
from parameterized import parameterized # type: ignore
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
    def test_access_nested_map_exception(self, nested_map, path, expected_error):
        """A method to test the nested map"""
        with self.assertRaises(KeyError) as key_error:
            access_nested_map(nested_map, path)
            nest_exception = key_error.exception
            self.assertEqual(expected_error, nest_exception)