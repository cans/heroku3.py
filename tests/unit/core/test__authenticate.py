# -*- coding: utf-8; -*-
from __future__ import absolute_import, division, print_function
from unittest import mock

from heroku3.api import Heroku
from heroku3.core import _authenticate


@mock.patch('heroku3.core.Heroku')
def test__authenticate_with_login_password(heroku_class, login_name, login_secret):
    # with mock.patch.object(heroku_core, 'authenticate') as authenticate_method:
    hk_client = _authenticate(login_name, login_secret)

    hk_client.authenticate.assert_called_once_with(login_name, login_secret)
    assert hk_client._session is not None


@mock.patch('heroku3.core.Heroku')
def test__authenticate_with_api_key(heroku_class, heroku_api_key):
    # with mock.patch.object(heroku_core, 'authenticate') as authenticate_method:
    hk_client = _authenticate('', heroku_api_key)

    hk_client.authenticate.assert_called_once_with('', heroku_api_key)
    assert hk_client._session is not None


@mock.patch('heroku3.core.Heroku')
def test__authenticate_with_api_key(heroku_class, heroku_api_key):
    session = object()
    hk_client = _authenticate('', heroku_api_key, session=session)

    hk_client.authenticate.assert_called_once_with('', heroku_api_key)
    assert hk_client._session.auth is not None


# vim: et:sw=4:syntax=python:ts=4:
