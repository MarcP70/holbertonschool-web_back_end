#!/usr/bin/env python3
""" Module of basic authentification """
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ Basic authentification class """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ Extracts and returns the Base64 part of the Authorization
            header for Basic Authentication.
        """
        if authorization_header is None or not isinstance(
                authorization_header, str):
            return None

        # Check if the header starts with 'Basic ' (with space at the end)
        if not authorization_header.startswith('Basic '):
            return None

        # Extract the Base64 part after 'Basic ' (which is 6 characters long)
        base64_credentials = authorization_header[6:].strip()

        return base64_credentials
