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


Usage
-----

.. code-block:: bash

    $ http http+unix://%2Ftmp%2Fprofilesvc.sock/status/pid


Requirements
------------

- requests-unixsocket_

.. _requests-unixsocket: https://github.com/msabramo/requests-unixsocket/
