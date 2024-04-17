#!/usr/bin/env python3
"""
The base authentication module.
"""
from flask import request
from typing import List, TypeVar
import fnmatch


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
        if path is None:
            return True
        if not excluded_paths or excluded_paths is None:
            return True
        for excluded_path in excluded_paths:
            if path[-1] != "/":
                path = path + "/"
            if fnmatch.fnmatch(path, excluded_path):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Method to get authorization header.
        """
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Method to get user from the request.
        """
        return None
