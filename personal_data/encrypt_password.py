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
