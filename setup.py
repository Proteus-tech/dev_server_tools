#!/usr/bin/env python

from distutils.core import setup

setup(name='dev_server_tools',
      version='1.1',
      description='dev server tools for Django',
      author='Proteus Technologies',
      author_email='team@proteus-tech.com',
      url='http://proteus-tech.com',
      packages=['dev_server_tools', 'dev_server_tools.management', 'dev_server_tools.management.commands'],
     )