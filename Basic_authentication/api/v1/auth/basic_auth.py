#!/usr/bin/env python3
""" Module of basic authentification """
from typing import TypeVar
import base64
from api.v1.auth.auth import Auth
from models.user import User


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

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ Extracts user email and password from a decoded Base64
            authorization header.
        """
        if decoded_base64_authorization_header is None or not isinstance(
                decoded_base64_authorization_header, str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        Returns the User instance based on email and password.
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        # Search for the user in the database
        user_instance = User.search({"email": user_email})
        if not user_instance:
            return None

        # Assuming `search` returns a list of users,
            # we should take the first user.
        user_instance = user_instance[0]

        # Check if the provided password matches the user's stored password
        if not user_instance.is_valid_password(user_pwd):
            return None

        return user_instance
