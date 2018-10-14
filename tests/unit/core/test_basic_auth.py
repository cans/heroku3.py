# -*- coding: utf-8; -*-
from __future__ import absolute_import, division, print_function
from unittest import mock

from heroku3.core import basic_auth


@mock.patch('heroku3.core._authenticate')
def test_basic_auth(_authenticate_func, login_name, login_secret):
    hk_client = basic_auth(login=login_name, secret=login_secret)

    _authenticate_func.assert_called_once_with(login_name,
                                               login_secret,
                                               session=None,
                                               trust_env=True,
                                               )


@mock.patch('heroku3.core._authenticate')
def test_basic_auth_with_api_key_and_session(_authenticate_func,
                                             login_name,
                                             login_secret,
                                             ):
    session = object()
    hk_client = basic_auth(login=login_name,
                           secret=login_secret,
                           session=session)

    _authenticate_func.assert_called_once_with(login_name,
                                               login_secret,
                                               session=session,
                                               trust_env=True,
                                               )


@mock.patch('heroku3.core._authenticate')
def test_basic_auth_with_api_key_and_session_and_trust_env(_authenticate_func,
                                                           login_name,
                                                           login_secret,
                                                           ):
    session = object()
    trust_env = False
    hk_client = basic_auth(login=login_name,
                           secret=login_secret,
                           session=session,
                           trust_env=trust_env,
                           )

    _authenticate_func.assert_called_once_with(login_name,
                                               login_secret,
                                               session=session,
                                               trust_env=trust_env,
                                               )


# vim: et:sw=4:syntax=python:ts=4:
