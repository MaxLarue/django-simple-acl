import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

setup(
    name='django-simple-acl',
    version='0.1.0',
    packages=['simpleacls'],
    description='Access control lists tied to django groups',
    long_description=README,
    author='MaxLarue',
    author_email='maximilienlarue@gmail.com',
    url='https://github.com/MaxLarue/django-simple-acl/',
    license='MIT',
    install_requires=[
        'Django>=2.7',
    ]
)