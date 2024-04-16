#!/usr/bin/env python3
"""
The base authentication module.
"""
from flask import request


class Auth:
    """
    The Authentication Class.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Method to check if auth is required.
        Args:
            path :- the url to check
            excluded_paths :- list of excluded paths
        """
        return False


    def authorization_header(self, request=None) -> str:
        """
        Method to get authorization header.
        """
        return None


    def current_user(self, request=None) -> TypeVar('User'):
        """
        Method to get user from the request.
        """
        return None
