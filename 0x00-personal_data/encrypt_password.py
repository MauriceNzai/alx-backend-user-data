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
