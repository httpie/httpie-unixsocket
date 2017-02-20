httpie-unixsocket
=================

UNIX socket transport plugin for `HTTPie <http://httpie.org>`_.

.. image:: https://badge.fury.io/py/httpie-unixsocket.svg
    :target: https://badge.fury.io/py/httpie-unixsocket
    :alt: Latest Version on PyPI
    
    
Installation
------------

.. code-block:: bash

    $ pip install httpie-unixsocket


Example usage
-------------

To query Docker for info, using `/var/run/docker.sock`:

.. code-block:: bash

    $ http http+unix://%2Fvar%2Frun%2Fdocker.sock/info


Requirements
------------

- requests-unixsocket_

.. _requests-unixsocket: https://github.com/msabramo/requests-unixsocket/
