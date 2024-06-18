#!/usr/bin/env python3
""" Module of basic authentification """
import base64
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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ Decodes a Base64-encoded string and returns it as UTF-8 string """
        if base64_authorization_header is None or not isinstance(
                base64_authorization_header, str):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_string = decoded_bytes.decode('utf-8')
            return decoded_string
        except (base64.binascii.Error, UnicodeDecodeError):
            return None
