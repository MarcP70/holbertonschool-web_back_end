#!/usr/bin/env python3
""" Module of authentification
"""
from typing import List
from flask import request


class Auth:
    """ Authentification class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Returns True if path is None
        Returns True if excluded_paths is None or empty
        Returns False if path is in excluded_paths
        """
        if not path:
            return True

        if not excluded_paths or len(excluded_paths) == 0:
            return True

        # Check if path is in excluded_paths
        for excluded_path in excluded_paths:
            # Normalize paths to be slash tolerant
            if path.rstrip('/') == excluded_path.rstrip('/'):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Returns None """
        return None

    def current_user(self, request=None) -> str:
        """ Returns None """
        return None
