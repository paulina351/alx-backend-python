#!/usr/bin/env python3
"""Parameterize and patch as decorators
   Mocking a property
   More patching
   Parameterize
   Integration test: fixtures
   Integration tests
"""

import unittest
from parameterized import parameteriized, parameterized_class  # type: ignore
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """A class that ingerit from githuborg."""
    @parameteriized.expand([
        "google",
        "abc"])
    @patch("client_get_json")
    def test_org(self, name_org, mock_url):
        """Method that test the githuborg."""
        endpoint = "https://api.github.com/orgs/{}".format(name_org)
        get_org = GithubOrgClient(name_org)
        self.assertEqual(get_org.org, mock_url.return_value)
        mock_url.assert_called_once_with(endpoint)

    def test_public_repos_url(self):
        """A method that test for github public repo url."""
        mock_url = "www.someurl.com"
        the_payload = {"repos_url": mock_url}
        with patch('client.GithubOrgClient.org',
                   PropertyMock(return_value=the_payload)):
            res = GithubOrgClient("somewhere")
            self.assertEqual(res._public_repos_url, mock_url)
