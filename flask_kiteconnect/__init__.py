# -*- coding: utf-8 -*-
"""
    __init__.py

    :copyright: (c) 2017 by Joe Paul.
    :license: see LICENSE for details.
"""
from kiteconnect import KiteConnect


__all__ = ('FlaskKiteConnect', )
__version__ = '0.1.0'


class FlaskKiteConnect(object):
    """
        Flask extension for kiteconnect api

        app = Flask(__name__)
        kiteconnect = FlaskKiteConnect(app)

    """

    def __init__(self, app=None):
        self._client = None

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """Initialize the kiteconnect client

        :param app: Flask app instance
        """
        self._client = KiteConnect(
            app.config.get('KITECONNECT_API_KEY')
        )
        access_token = app.config.get('KITECONNECT_ACCESS_TOKEN')
        if access_token:
            self._client.set_access_token(access_token)

    def __getattr__(self, name):
        """Proxy methods to the private held object
        """
        return getattr(self._client, name)
