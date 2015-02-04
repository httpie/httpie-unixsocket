httpie-unixsocket
=================

UNIX socket plugin for `HTTPie <https://github.com/jkbr/httpie>`_.


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
