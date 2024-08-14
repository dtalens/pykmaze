#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2008-2011 Emmanuel Blot <emmanuel.blot@free.fr>
# Modified 2024: Dani Talens <databio@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from setuptools import setup  # Canvi de distutils.core a setuptools

def _read(fname):
    import os
    with open(os.path.join(os.path.dirname(__file__), fname), encoding='utf-8') as f:  # afegit encoding per compatibilitat amb Python 3
        return f.read()

setup(
    name='pykmaze',
    version='0.2.0',
    description='Keymaze 500-700 communicator',
    author='Emmanuel Blot',
    author_email='emmanuel.blot@free.fr',
    license='MIT',
    keywords='keymaze geonaute kml kmz gps',
    url='http://github.com/dtalens/pykmaze',
    download_url='https://github.com/dtalens/pykmaze/tarball/master',
    packages=['pykmaze'],
    install_requires=['pyserial>=2.5'],  # canvi de requires a install_requires
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Healthcare Industry',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
        'Topic :: Utilities'
    ],
    long_description=_read('README.rst'),
)
