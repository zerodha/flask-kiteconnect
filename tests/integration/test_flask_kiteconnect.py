# -*- coding: utf-8 -*-
"""
    integration/test_flask_kiteconnect.py

    :copyright: (c) 2017 by Joe Paul.
    :license: see LICENSE for details.
"""
import flask
import pytest
from flask_kiteconnect import FlaskKiteConnect


@pytest.fixture()
def app():
    return flask.Flask(__name__)


def test_constructor(app):
    kiteconnect = FlaskKiteConnect(app)
    assert kiteconnect._client is not None
    # Make sure that getattr magic meth works
    assert kiteconnect._default_root_uri == 'https://api.kite.trade'


def test_init_app(app):
    """Test that a constructor without app instance will not initialize the
    connection. After FlaskKiteConnect.init_app(app) is called,
    the connection will be initialized.
    """
    kiteconnect = FlaskKiteConnect()
    assert kiteconnect._client is None
    kiteconnect.init_app(app)
    assert kiteconnect._client is not None
