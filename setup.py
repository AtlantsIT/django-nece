# -*- coding: utf-8 -*-
from setuptools import setup
from pip.req import parse_requirements

with open('README.rst') as f:
    ld = f.read()

long_description = ld.replace(ld[0:ld.find('nece?')], '')

version = '0.7.0'
description = "A content translation framework using Postgresql's jsonb" + \
    " field in the background"
url = 'https://github.com/tatterdemalion/django-nece'
download_url = '/'.join([url, 'tarball', version])

install_reqs = parse_requirements('requirements.txt')


setup(
    name='nece',
    version=version,
    description=description,
    long_description=long_description,
    author='Can Mustafa Özdemir',
    author_email='canmustafaozdemir@gmail.com',
    url=url,
    download_url=download_url,
    keywords=['translations', 'i18n', 'language', 'multilingual'],
    packages=['nece'],
    install_requires = [str(ir.req) for ir in install_reqs],
    license='BSD License',
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Database",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Text Processing :: Linguistic",
    ],
)
