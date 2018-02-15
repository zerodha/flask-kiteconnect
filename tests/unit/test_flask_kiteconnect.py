# -*- coding: utf-8 -*-
"""
    unit/test_flask_kiteconnect.py

    :copyright: (c) 2017 by Joe Paul.
    :license: see LICENSE for details.
"""
from flask_kiteconnect import FlaskKiteConnect


def test_constructor_app(mocker):
    """Test that the constructor passes the app to FlaskKiteConnect.init_app
    """
    mocker.patch.object(FlaskKiteConnect, 'init_app', autospec=True)
    app_stub = mocker.stub(name='app_stub')
    FlaskKiteConnect(app_stub)
    FlaskKiteConnect.init_app.assert_called_once_with(mocker.ANY, app_stub)
