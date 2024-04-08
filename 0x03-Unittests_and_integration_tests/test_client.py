#!/usr/bin/env python3
"""testing module for testing the client module.
"""
from typing import Dict
from parameterized import parameterized, parameterized_class
import unittest
from unittest.mock import Mock, MagicMock,,PropertyMock,patch 
from requests import HTTPError

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """class for testing GithubOrgClient"""
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch(
        "client.get_json",
    )
    def test_org(self, org: str, resp: Dict, _mocked_function: MagicMock) -> None:
        """ method to test org """
        _mocked_function.return_value = MagicMock(return_value=resp)
        github_org_client = GithubOrgClient(org)
        self.assertEqual(github_org_client.org(), resp)
        _mocked_function.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )

    def test_public_repos_url(self) -> None:
        """method for testing _public_repos_url"""
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock,
                ) as _mock_organiz:
            _mock_organiz.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )

    @patch("client.get_json")
    def test_public_repos(self, __get_json_mock: MagicMock) -> None:
        """method for testing public_repos """
        test_payload = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [
                {
                    "id": 7697149,
                    "name": "episodes.dart",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/episodes.dart",
                    "created_at": "2013-01-19T00:31:37Z",
                    "updated_at": "2019-09-23T11:53:58Z",
                    "has_issues": True,
                    "forks": 22,
                    "default_branch": "master",
                },
                {
                    "id": 8566972,
                    "name": "kratu",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/kratu",
                    "created_at": "2013-03-04T22:52:33Z",
                    "updated_at": "2019-11-15T22:22:16Z",
                    "has_issues": True,
                    "forks": 32,
                    "default_branch": "master",
                },
            ]
        }
        __get_json_mock.return_value = test_payload["repos"]
        with patch(
                "client.GithubOrgClient._public_repos_url",
                new_callable=PropertyMock,
                ) as _public_repos_url_mock:
            _public_repos_url_mock.return_value = test_payload["repos_url"]
            self.assertEqual(
                GithubOrgClient("google").public_repos(),
                [
                    "episodes.dart",
                    "kratu",
                ],
            )
            _public_repos_url_mock.assert_called_once()
        __get_json_mock.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': "bsd-3-clause"}}, "bsd-3-clause", True),
        ({'license': {'key': "bsl-1.0"}}, "bsd-3-clause", False),
    ])
    def test_has_license(self, repo: Dict, key: str, expected: bool) -> None:
        """method for testing has_license """
        github_org_client = GithubOrgClient("google")
        client_has_licence = github_org_client.has_license(repo, key)
        self.assertEqual(client_has_licence, expected)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ integration test class for GithubOrgClient """
    @classmethod
    def setUpClass(cls) -> None:
        """ method to make  class fixtures for testing."""
        payload_for_routing = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def return_payload(url):
          """helper function"""
            if url in payload_for_routing:
                return Mock(**{'json.return_value': payload_for_routing[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=return_payload)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """method for testing public_repos """
        self.assertEqual(
            GithubOrgClient("google").public_repos(),
            self.expected_repos,
        )

    def test_public_repos_with_license(self) -> None:
        """method to tests the public_repos with licences"""
        self.assertEqual(
            GithubOrgClient("google").public_repos(license="apache-2.0"),
            self.apache2_repos,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """method to tear down class fixtures after testing."""
        cls.get_patcher.stop()
