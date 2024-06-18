#!/usr/bin/env python3
""" Module of authentification
"""
from typing import List
from flask import request


class Auth:
    """ Authentification class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Returns False for now """
        return False

    def authorization_header(self, request=None) -> str:
        """ Returns None """
        return None

    def current_user(self, request=None) -> str:
        """ Returns None """
        return None
