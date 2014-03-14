#!/usr/bin/env python3

from distutils.core import setup

setup(data_files=['COPYING'],
      description='Sensor network attack simulation',
      maintainer='Michael Catanzaro',
      maintainer_email='michael.catanzaro@mst.edu',
      py_modules=['sensor'],
      name='RKP Attack',
      requires=['networkx', 'matplotlib'],
      scripts=['rkp-attack'],
      url='https://github.com/lmnn3/rkp-attack',
      version='0.1',
     )
