#!/usr/bin/env python3
"""
Base SessionAuth class
"""
from uuid import uuid4

from .auth import Auth


class SessionAuth(Auth):
    """
    Session Authorization protocol class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a Session ID for a user with given id (user_id)
        Args:
            user_id (str): user's user id to create a session for
        Return:
            None if user_id is None or not a string
            str - Session ID for the user
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        id = uuid4()
        self.user_id_by_session_id[str(id)] = user_id
        return str(id)

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Returns the user ID based on a session ID
        Args:
            session_id (str): the session ID
        Return:
            user id (str) or None if session_id is None or not a string
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)
