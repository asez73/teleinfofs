#!/usr/bin/env python

from distutils.core import setup

open("fusepy/__init__.py","w").close()

setup(name='TeleinfoFS',
      version='0.1',
      description='Systeme de fichier pour acceder au compteur electrique',
      author='Radim Badsi',
      author_email='radim@badsi.info',
      url='http://code.google.com/p/teleinfofs/',
      py_modules=['teleinfo','fusepy.fuse'],
      scripts=['teleinfofs.py'],
     )
