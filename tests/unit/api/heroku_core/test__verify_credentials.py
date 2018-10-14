# -*- coding: utf-8; -*-
from __future__ import absolute_import, division, print_function
from unittest.mock import patch


def test___verify_credentials(heroku_core_w_session):
    url = 'http://example.com'
    with patch.object(heroku_core_w_session,
                      '_url_for',
                      return_value=url) as _url_for_method, \
         patch.object(heroku_core_w_session._session, 'get') as get_method:
        heroku_core_w_session._verify_credentials()

    get_method.assert_called_once_with(url)

