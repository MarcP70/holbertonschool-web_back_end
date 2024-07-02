#!/usr/bin/env python3
"""Use unit tests to ensure it correctly accesses values.
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


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
        with patch.object(GithubOrgClient, 'org', new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {
                "repos_url": "https://api.github.com/orgs/test-org/repos"}

            client = GithubOrgClient("test-org")
            result = client._public_repos_url

            # Vérifie que le résultat est l'URL attendue
            self.assertEqual(
                result, "https://api.github.com/orgs/test-org/repos")

if __name__ == "__main__":
    unittest.main()
