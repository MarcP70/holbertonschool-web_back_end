#!/usr/bin/env python3
"""
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """This class contains unit tests to ensure it correctly accesses values
        in a nested map using a sequence of keys.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map with various nested maps and paths.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test access_nested_map raises KeyError for invalid paths.
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test case for the utils.get_json function.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, url, expected_payload):
        """Test get_json function to ensure it returns expected JSON data.
        """
        with patch('requests.get') as mock_request:
            # Configure the mock to return the expected payload
            mock_request.return_value.json.return_value = expected_payload

            # Call the function with the test URL
            result = get_json(url)

            # Verify that requests.get was called with the correct URL
            mock_request.assert_called_once_with(url)

            # Verify that the result matches the expected payload
            self.assertEqual(result, expected_payload)


if __name__ == "__main__":
    unittest.main()
