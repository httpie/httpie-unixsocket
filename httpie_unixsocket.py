"""
UNIX socket plugin for HTTPie.

"""
from httpie.plugins import AuthPlugin
import requests_unixsocket


__version__ = '0.0.0'
__author__ = 'Marc Abramowitz'
__licence__ = 'BSD'


requests_unixsocket.monkeypatch()


class UnixSocketAuthPlugin(AuthPlugin):
    name = 'UNIX socket'
