# -*- coding: utf-8 -*-

"""
heroku3.core
~~~~~~~~~~~

This module provides the base entrypoint for heroku3.py.
"""

import requests

from .api import Heroku


def from_key(api_key=None, session=None, trust_env=False, **kwargs):
    """Returns an authenticated Heroku instance, via API Key."""
    return _authenticate('', api_key, session=session, trust_env=trust_env, **kwargs)


def basic_auth(login=None, secret=None, session=None, trust_env=True, **kwargs):
    """Returns an authenticated Heroku instance, via login/password.

    This function can retrieve credentials from your :file:`~/.netrc` file.

    Args:
        login (str | None): the user's login name
        secret (str | None): the user's secret (password, token or API key)
        session (requests.Session | None): session to store cookies, credentials, ...

    """
    return _authenticate(login, secret, session=session, trust_env=trust_env, **kwargs)


def _authenticate(login, secret, session=None, trust_env=False, **kwargs):
    """Returns an authenticated Heroku client instance

    Args:
        login (str): the user's login (or '' if using API Key auth.)
        secret (str): the user's secret (API Key, Auth token, ...)
        session (requests.Session | None): storage for credential, cookies, etc.

    Returns:
        heroku3.api.Heroku: an authenticated Heroku client.
    """
    if session is None:
        session = requests.session()
        session.trust_env = trust_env

    h = Heroku(session=session, **kwargs)

    # Login.
    h.authenticate(login, secret)

    return h


# vim: et:sw=4:syntax=python:ts=4:
