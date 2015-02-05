"""
UNIX socket transport plugin for HTTPie.

"""
from httpie.plugins import TransportPlugin
from requests_unixsocket import UnixAdapter, DEFAULT_SCHEME


__version__ = '0.0.0'
__author__ = 'Marc Abramowitz'
__licence__ = 'BSD'


class UnixSocketTransportPlugin(TransportPlugin):
    name = 'UNIX socket transport'

    prefix = DEFAULT_SCHEME

    def get_adapter(self):
        return UnixAdapter()
