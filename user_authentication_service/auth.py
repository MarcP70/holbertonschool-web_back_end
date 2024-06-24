#!/usr/bin/env python3
"""Auth module
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """Hash a password string using bcrypt and return the salted hash."""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


def _generate_uuid() -> str:
    """Generate a string representation of a new UUID."""
    return uuid.uuid4().hex


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user if the email does not exist,
            else raise ValueError.
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """Validate the authentification of email and password provided
        """
        try:
            user = self._db.find_user_by(email=email)
            stored_hashed_password = user.hashed_password

            # Check if the provided password matches the stored hashed password
            if bcrypt.checkpw(password.encode('utf-8'),
                              stored_hashed_password):
                return True
            else:
                return False

        except NoResultFound:
            return False
