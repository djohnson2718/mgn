Installation
==============

The module is distributed on PyPI. You just need to run the following command: ::

    $ sage -pip install surface_dynamics [--user]

The –user option is optional and allows to install the module in your user space (and does not require administrator rights). 

If that doesn't work try updating sage (some earlier versions of sage are packaged with an incompatible version of PyPI.)

If that still fails, try downloading the source, extracting it, opening a terminal in the directory that has the ``setup.py`` file, and run: ::

    $ sage setup.py -install

mgn Package
============

The ``mgn`` package contains two modules for computations on the moduli space of curves.

strataalgebra
==============

This module computes product in the strata algebra. It also contains some of A. Pixton's code to compute FZ relations. 
