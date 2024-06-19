#!/usr/bin/env python3
""" Module of authentification """
from typing import List
from flask import request
import os


class Auth:
    """ Authentification class """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Checks if authentication is required for the given path """
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
        """ Returns the Authorization header value from the request """
        if not request:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> str:
        """ Returns None """
        return None

    def session_cookie(self, request=None) -> str:
        """ Returns the value of the session cookie from the provided
            request object.
        """
        if request is None:
            return None

        # Retrieve the cookie name from the environment variable
        session_name = os.getenv('SESSION_NAME', '_my_session_id')

        # Return the value of the session cookie
        return request.cookies.get(session_name)
