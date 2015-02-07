httpie-unixsocket
=================

UNIX socket transport plugin for `HTTPie <http://httpie.org>`_.

.. image:: https://pypip.in/version/httpie-unixsocket/badge.svg
    :target: https://pypi.python.org/pypi/httpie-unixsocket/
    :alt: Latest Version


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
