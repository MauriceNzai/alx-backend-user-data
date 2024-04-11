#!/usr/bin/env python3
"""
encrypting and validating passwords.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password and adds random salt.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    validates provided password against the stored hashed password.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
