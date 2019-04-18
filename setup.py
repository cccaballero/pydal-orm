import re
import ast
from setuptools import setup

setup(
    name='weppy',
    version=version,
    url='http://github.com/cccaballero/pydal-orm/',
    description='PyDal bassed ORM extracted from Weppy framework',
    long_description='PyDal bassed ORM extracted from Weppy framework',
    packages=[
        'pydal_orm', 'pydal_orm.migrations',
    ],
    platforms='any',
    install_requires=[
        'pyDAL==17.3',
    ],
    classifiers=[
    ]
)
