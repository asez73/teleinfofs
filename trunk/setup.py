#!/usr/bin/env python

from distutils.core import setup

setup(name='TeleinfoFS',
      version='0.1',
      description='Systeme de fichier pour acceder au compteur electrique',
      author='Radim Badsi',
      author_email='radim@badsi.info',
      url='http://code.google.com/p/teleinfofs/',
      packages=['teleinfofs','fusepy'],
      package_dir={'teleinfofs': 'teleinfofs',
      		   'fusepy': 'fusepy'},
     )
