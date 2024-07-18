"""
Example python package
"""

import re
import ast
from setuptools import setup, find_packages


_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('examplepackage/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    name='example-python-package',
    version=version,
    url='https://github.com/tim-s-ccs/example-python-package',
    license='MIT',
    author='Tim South',
    description='Example python package description',
    long_description=__doc__,
    packages=find_packages(),
    install_requires=[
    ],
    python_requires=">=3.9,<3.13",
)
