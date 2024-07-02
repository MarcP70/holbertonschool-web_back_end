#!/usr/bin/env python3
"""Use unit tests to ensure it correctly accesses values.
"""
import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
    Classe de test pour vérifier le fonctionnement de GithubOrgClient.
    """

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Teste que GithubOrgClient.org retourne la valeur correcte.
        """
        # Mock retour de get_json
        mock_get_json.return_value = {"key": "value"}

        # Initialise l'objet GithubOrgClient avec org_name
        client = GithubOrgClient(org_name)

        # Appele la méthode org
        result = client.org

        # Vérifie que get_json a été appelé une fois avec l'URL attendue
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

        # Vérifie que le résultat est celui attendu
        self.assertEqual(result, {"key": "value"})

    def test_public_repos_url(self):
        """
        Teste que _public_repos_url retourne la bonne URL
        basée sur la valeur mockée de org.
        """
        with patch.object(GithubOrgClient, 'org',
                          new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {
                "repos_url": "https://api.github.com/orgs/test-org/repos"}

            client = GithubOrgClient("test-org")
            result = client._public_repos_url

            # Vérifie que le résultat est l'URL attendue
            self.assertEqual(
                result, "https://api.github.com/orgs/test-org/repos")

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        Teste que public_repos retourne la liste de repos attendue
        et que les méthodes mockées sont appelées une fois.
        """
        # Payload mocké pour get_json
        mock_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]
        mock_get_json.return_value = mock_payload

        # Mock de _public_repos_url
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = \
                "https://api.github.com/orgs/test-org/repos"

            client = GithubOrgClient("test-org")
            result = client.public_repos()

            # Vérifier que la liste des repos est celle attendue
            expected_repos = ["repo1", "repo2", "repo3"]
            self.assertEqual(result, expected_repos)

            # Vérifier que la propriété mockée et get_json ont été appelées
            #  une fois
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/test-org/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Teste que has_license retourne la valeur attendue.
        """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class([
    {"org_payload": TEST_PAYLOAD[0][0],
     "repos_payload": TEST_PAYLOAD[0][1],
     "expected_repos": TEST_PAYLOAD[0][2],
     "apache2_repos": TEST_PAYLOAD[0][3]}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """TestIntegrationGithubOrgClient class
    """

    @classmethod
    def setUpClass(cls):
        """
        A class method called before tests
        in an individual class are run.
        """
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()
        mock_response_org = Mock()
        mock_response_org.json.return_value = cls.org_payload

        mock_response_repos = Mock()
        mock_response_repos.json.return_value = cls.repos_payload

        cls.mock_get.side_effect = [
            mock_response_org,
            mock_response_repos,
            mock_response_org,
            mock_response_repos
        ]

    @classmethod
    def tearDownClass(cls):
        """
        A class method called after tests
        in an individual class have run
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Tests the public_repos method
        """
        client = GithubOrgClient("google")
        result = client.public_repos()
        self.assertEqual(result, self.expected_repos)

    def test_public_repos_with_license(self):
        """Tests the public_repos method with a license
        """
        client = GithubOrgClient("google")
        result = client.public_repos("apache-2.0")
        self.assertEqual(result, self.apache2_repos)


if __name__ == "__main__":
    unittest.main()
