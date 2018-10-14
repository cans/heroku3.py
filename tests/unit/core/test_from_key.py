# -*- coding: utf-8; -*-
from __future__ import absolute_import, division, print_function
from unittest import mock

from heroku3.core import from_key


@mock.patch('heroku3.core._authenticate')
def test_from_key_with_api_key(_authenticate_func, heroku_api_key):
    hk_client = from_key(heroku_api_key)

    _authenticate_func.assert_called_once_with('',
                                               heroku_api_key,
                                               session=None,
                                               trust_env=False
                                               )


@mock.patch('heroku3.core._authenticate')
def test_from_key_with_api_key_and_session(_authenticate_func, heroku_api_key):
    session = object()
    hk_client = from_key(heroku_api_key, session=session)

    _authenticate_func.assert_called_once_with('',
                                               heroku_api_key,
                                               session=session,
                                               trust_env=False,
                                               )


@mock.patch('heroku3.core._authenticate')
def test_from_key_with_api_key_and_session_and_trust_env(_authenticate_func,
                                                         heroku_api_key,
                                                         ):
    session = object()
    trust_env = True
    hk_client = from_key(heroku_api_key, session=session, trust_env=trust_env)

    _authenticate_func.assert_called_once_with('',
                                               heroku_api_key,
                                               session=session,
                                               trust_env=trust_env,
                                               )


# vim: et:sw=4:syntax=python:ts=4:
