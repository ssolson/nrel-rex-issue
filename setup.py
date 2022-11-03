from setuptools import setup, find_packages
from distutils.core import Extension
import os
import re

DISTNAME = 'nrel-issue'
PACKAGES = find_packages()
EXTENSIONS = []
DESCRIPTION = 'Test to run nrel-rex'
AUTHOR = 'ssolson'
MAINTAINER_EMAIL = ''
LICENSE = 'Revised BSD'
URL = ''
CLASSIFIERS = ['Development Status :: 3 - Alpha',
               'Programming Language :: Python :: 3',
               'Topic :: Scientific/Engineering',
               'Intended Audience :: Science/Research',
               'Operating System :: OS Independent',
               ]
DEPENDENCIES = ['NREL-rex']
LONG_DESCRIPTION = 'ssolson'
VERSION='2022.11.03'

setup(name=DISTNAME,
      version=VERSION,
      packages=PACKAGES,
      ext_modules=EXTENSIONS,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      author=AUTHOR,
      maintainer_email=MAINTAINER_EMAIL,
      license=LICENSE,
      url=URL,
      classifiers=CLASSIFIERS,
      zip_safe=False,
      install_requires=DEPENDENCIES,
      scripts=[],
      include_package_data=True
      )
