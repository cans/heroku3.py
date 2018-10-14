# -*- coding: utf-8; -*-
from __future__ import absolute_import, division, print_function
from unittest.mock import patch


def test_heroku_core_authenticate_with_api_key(heroku_core,
                                               heroku_api_key,
                                               ):
    with patch.object(heroku_core, '_verify_api_key') as _verify_api_key_method:
        heroku_core.authenticate('', heroku_api_key)

    assert heroku_core._session is not None
    assert _verify_api_key_method.called

def test_heroku_core_authenticate_with_login_(heroku_core,
                                              login_name,
                                              login_secret,
                                              ):
    with patch.object(heroku_core, '_verify_api_key') as _verify_api_key_method:
        heroku_core.authenticate(login_name, login_secret)

    assert _verify_api_key_method.called
