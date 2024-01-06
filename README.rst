
Colored Print
-------------


.. image:: https://img.shields.io/pypi/v/python-colored-print
   :target: https://pypi.org/project/python-colored-print/
   :alt: PyPI


.. image:: https://img.shields.io/pypi/pyversions/python-colored-print
   :target: https://pypi.org/project/python-colored-print/
   :alt: Python Versions


.. image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://raw.githubusercontent.com/agn-7/colored-print/master/LICENSE
   :alt: GitHub license


A lightweight python library in order to print in different colors and save them into a file optionally.

Setup
-----

.. code-block:: bash

   pip install python-colored-print

Usage
-----

.. code-block:: python

   from colored_print import log

   log.success("Hello", 123, "Bye").store()
   log.info("Hello", 123, "Bye")
   log.warn("Hello", 123, "Bye")
   log.err("Hello", 123, "Bye").store()
   log.pink("Hello", 123, "Bye")
   log("Hello", 123, "Bye")  # default color is white

Output
------


.. image:: https://i.stack.imgur.com/HMVP6.png
   :target: https://i.stack.imgur.com/HMVP6.png
   :alt: Output

