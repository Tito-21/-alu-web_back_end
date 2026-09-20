#!/usr/bin/env python3
"""Encrypt password module"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Return a salted, hashed password as a byte string"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
