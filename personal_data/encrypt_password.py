#!/usr/bin/env python3
"""
Task 5: Encrypting passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt with a salt.

    Args:
        password (str): The password to hash.

    Returns:
        bytes: Salted and hashed password as a byte string.
    """
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Checks if a password matches a hashed password using bcrypt.

    Args:
        hashed_password (bytes): The hashed password stored in the database.
        password (str): The plaintext password to check.

    Returns:
        bool: True if the password matches the hashed password, False otherwise
    """
    # Check if the provided password matches the hashed password
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
