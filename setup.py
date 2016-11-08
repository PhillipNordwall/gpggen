"""The setup for GPG Gen"""

import setuptools
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, 'README.rst'), encoding='UTF-8') as f:
    long_description = f.read()

setuptools.setup(
    name='gpggen',
    version='0.0.1a1',
    description='Generate GPG keys and save ones that contain words in a list'
    'of hex words.',
    long_description='',
    url='',
    author='Phillip Nordwall',
    author_email='Phillip.Nordwall+gpggen@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='random generator encryption',
    packages=setuptools.find_packages(exclude=['tests', 'venv']),
    install_requires=['docopt'],
    extras_require={
        'test': ['pytest'],
    },
    entry_points={
        'console_scripts': [
            'gpggen=gpggen.__main__:cli',
        ]
    }
)
