import sys

from setuptools import setup, find_packages
from colored_print import __version__


if sys.version_info[0] < 3:
    with open('README.rst') as f:
        long_description = f.read()
else:
    with open('README.rst', encoding='utf-8') as f:
        long_description = f.read()


setup(
    name='python_colored_print',
    version=__version__,
    description='A simple python library in order to print in different colors'
                'and save them into a file optionally.',
    long_description=long_description,
    url='https://github.com/agn-7/colored-print',
    author='agn-7',
    author_email='benyaminjmf@gmail.com',
    license='MIT',
    packages=find_packages(),
    keywords=[
        'log',
        'logging',
        'python3',
        'python',
    ],
    download_url='https://github.com/agn-7/colored-print/archive/refs/tags/v1.0.0-rc1.zip',
    install_requires=[
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
