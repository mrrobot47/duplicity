.. duplicity documentation master file, created by
   sphinx-quickstart on Wed Jul 31 10:32:30 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to duplicity's documentation!
=====================================

.. topic:: Introduction

    Duplicity backs directories by producing encrypted tar-format volumes and uploading
    them to a remote or local file server. Because duplicity uses librsync, the incremental
    archives are space efficient and only record the parts of files that have changed since
    the last backup. Because duplicity uses GnuPG to encrypt and/or sign these archives,
    they will be safe from spying and/or modification by the server.


.. toctree:: modules
   :maxdepth: 4
   :caption: Table of Contents


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
